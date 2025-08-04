import google.generativeai as genai; import pandas as pd; import re
def summarize_articles(key,df):
    genai.configure(api_key=key); model=genai.GenerativeModel('gemini-1.5-flash'); summaries,keywords=[],[]
    prompt="""Analyze content and provide a summary and keywords. **Content:** "{content}" **Output Format:** Summary: [Your summary here] Keywords: [keyword1, keyword2]"""
    for _,r in df.iterrows():
        try:
            resp=model.generate_content(prompt.format(content=r['raw_content'][:2000]))
            s=re.search(r"Summary:(.*?)Keywords:",resp.text,re.DOTALL); k=re.search(r"Keywords:(.*)",resp.text,re.DOTALL)
            summaries.append(s.group(1).strip() if s else "N/A"); keywords.append(k.group(1).strip() if k else "")
        except: summaries.append("Error"); keywords.append("")
    df['summary']=summaries; df['keywords']=keywords
    return df
