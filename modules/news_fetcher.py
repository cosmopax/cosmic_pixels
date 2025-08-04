from newsapi import NewsApiClient; import pandas as pd
def fetch_news(key,q,from_d=None,to_d=None):
    n=NewsApiClient(api_key=key); a=n.get_everything(q=q,from_param=from_d,to=to_d,language='en',sort_by='relevancy',page_size=10)
    return pd.DataFrame([{'id':f"news_{i.get('title','')[:30]}",'source':'NewsAPI','title':i.get('title'),'url':i.get('url'),'raw_content':i.get('content')or i.get('description')or ''} for i in a.get('articles',[])])
