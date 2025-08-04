from googleapiclient.discovery import build
import pandas as pd

def _google_search(api_key, cse_id, query, **kwargs):
    """Helper function for Google Search."""
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, **kwargs).execute()
        return res.get('items', [])
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def fetch_google_search(api_key, cse_id, query):
    """Fetches web search results from Google Custom Search."""
    results = _google_search(api_key, cse_id, query, num=10)
    if not results:
        return pd.DataFrame()

    processed_results = []
    for item in results:
        processed_results.append({
            'id': f"gsearch_{item.get('cacheId', item.get('link'))}",
            'source': 'Google Search',
            'title': item.get('title'),
            'url': item.get('link'),
            'raw_content': item.get('snippet')
        })

    return pd.DataFrame(processed_results)

def fetch_google_images(api_key, cse_id, query):
    """Fetches image search results from Google Custom Search."""
    results = _google_search(api_key, cse_id, query, searchType='image', num=5)
    if not results:
        return pd.DataFrame()

    return pd.DataFrame([{'image_url': item['link']} for item in results])
