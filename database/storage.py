import sqlite3; import pandas as pd
DB_PATH = 'content_library.db'
def init_db():
    with sqlite3.connect(DB_PATH) as c: c.execute('''CREATE TABLE IF NOT EXISTS articles(id TEXT PRIMARY KEY,source TEXT,title TEXT,url TEXT,raw_content TEXT,summary TEXT,keywords TEXT,status TEXT DEFAULT 'new',fetch_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
def store_articles(df):
    if df.empty: return 0
    with sqlite3.connect(DB_PATH) as c:
        new = df[~df['id'].isin(pd.read_sql('SELECT id FROM articles',c)['id'].tolist())]
        if not new.empty: new.to_sql('articles',c,if_exists='append',index=False)
        return len(new)
def get_articles_by_status(s='new'):
    with sqlite3.connect(DB_PATH) as c: return pd.read_sql(f"SELECT * FROM articles WHERE status='{s}' ORDER BY fetch_date DESC", c)
def update_article_status(ids,s='selected'):
    with sqlite3.connect(DB_PATH) as c:
        placeholders = ','.join('?' for _ in ids)
        query = f"UPDATE articles SET status=? WHERE id IN ({placeholders})"
        c.execute(query, [s] + ids)
