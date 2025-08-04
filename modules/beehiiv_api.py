import requests
def create_newsletter_post(key,pub_id,title,md):
    h={"Authorization":f"Bearer {key}","Content-Type":"application/json"}; d={"title":title,"content":{"markdown":md},"status":"draft"}
    r=requests.post(f"https://api.beehiiv.com/v2/publications/{pub_id}/posts",json=d,headers=h)
    r.raise_for_status(); return r.json()
