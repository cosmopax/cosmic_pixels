import streamlit as st; import pandas as pd; import configparser; import datetime; from database import storage
st.set_page_config(page_title="Newsletter OS", page_icon="💡", layout="wide")
importers={}
def load_module(name):
    try: importers[name] = __import__(f"modules.{name}",fromlist=[name])
    except Exception as e: st.sidebar.warning(f"'{name}' module failed.",icon="⚠️"); importers[name]=None
[load_module(n) for n in ["news_fetcher","arxiv_fetcher","Google Search_fetcher","summarizer","beehiiv_api"]]
st.title("💡 Newsletter OS")
@st.cache_resource
def load_config():
    cfg=configparser.ConfigParser(); cfg.read('config.ini'); return cfg['API_KEYS']
try: api_keys=load_config(); storage.init_db()
except Exception as e: st.error(f"Config error: {e}"); st.stop()
with st.sidebar:
    st.header("1. Data Gathering"); q=st.text_input("Search Topic","longevity research")
    use_g=st.checkbox("Google",1,disabled=not importers["Google Search_fetcher"])
    use_n=st.checkbox("News",1,disabled=not importers["news_fetcher"])
    use_a=st.checkbox("ArXiv",1,disabled=not importers["arxiv_fetcher"])
    if st.button("Fetch & Digest",type="primary"):
        with st.spinner("Contacting sources..."):
            dfs=[]
            if use_g and importers["Google Search_fetcher"]: dfs.append(importers["Google Search_fetcher"].fetch_Google Search(api_keys['google_api_key'],api_keys['google_cse_id'],q))
            if use_n and importers["news_fetcher"]: dfs.append(importers["news_fetcher"].fetch_news(api_keys['news_api_key'],q))
            if use_a and importers["arxiv_fetcher"]: dfs.append(importers["arxiv_fetcher"].fetch_arxiv(q))
            if dfs:
                df=pd.concat(dfs,ignore_index=True).dropna(subset=['raw_content','title']).drop_duplicates(subset=['title'])
                if importers["summarizer"]: df=importers["summarizer"].summarize_articles(api_keys['google_api_key'],df)
                st.success(f"Stored {storage.store_articles(df)} new articles."); st.rerun()
st.header("2. Curation"); new_df=storage.get_articles_by_status('new')
if not new_df.empty:
    selected={r['id']:st.checkbox(f"**{r['title']}**",key=r['id']) for _,r in new_df.iterrows()}
    for _,r in new_df.iterrows():
        if selected[r['id']]:
            with st.container(border=True): st.caption(f"{r['source']} | {r['keywords']}"); st.markdown(r['summary'])
    if st.button("Queue Selected"): storage.update_article_status([i for i,s in selected.items() if s],'selected'); st.rerun()
st.header("3. Publication"); curated_df=storage.get_articles_by_status('selected')
if not curated_df.empty:
    if 'imgs' not in st.session_state: st.session_state.imgs={}
    title=st.text_input("Title",f"Digest: {pd.Timestamp.now().strftime('%B %d')}"); intro=st.text_area("Intro","Key developments this week:")
    for _,r in curated_df.iterrows():
        with st.container(border=True):
            st.markdown(f"**Article:** {r['title']}")
            if importers["Google Search_fetcher"]:
                imgs=importers["Google Search_fetcher"].fetch_google_images(api_keys['google_api_key'],api_keys['google_cse_id'],r['keywords']or r['title'])
                if not imgs.empty:
                    urls=["None"]+imgs['image_url'].tolist(); st.image(urls[1:],width=100)
                    st.session_state.imgs[r['id']]=st.radio("Img:",urls,key=f"r_{r['id']}",horizontal=True,format_func=lambda x:"None" if x=="None" else f"Img {urls.index(x)}")
    if st.button("Publish to Beehiiv",type="primary"):
        with st.spinner("Publishing..."):
            md=f"{intro}\n\n"
            for _,r in curated_df.iterrows():
                md+=f"## {r['title']}\n\n"
                if (img_url := st.session_state.imgs.get(r['id'])) and img_url != 'None': md+=f"![img]({img_url})\n\n"
                md+=f"*{r['summary']}*\n\n[Source]({r['url']})\n\n---\n\n"
            if importers["beehiiv_api"]:
                importers["beehiiv_api"].create_newsletter_post(api_keys['beehiiv_api_key'],api_keys['beehiiv_publication_id'],title,md)
                storage.update_article_status(curated_df['id'].tolist(),'published'); st.session_state.imgs={}; st.success("Draft sent!"); st.rerun()
