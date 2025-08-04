import arxiv; import pandas as pd
def fetch_arxiv(q,sort_by="SubmittedDate"):
    s=arxiv.Search(q,max_results=10,sort_by=getattr(arxiv.SortCriterion,sort_by,arxiv.SortCriterion.SubmittedDate))
    return pd.DataFrame([{'id':f"arxiv_{r.entry_id.split('/')[-1]}",'source':'ArXiv','title':r.title,'url':r.pdf_url,'raw_content':r.summary.replace('\n',' ')} for r in s.results()])
