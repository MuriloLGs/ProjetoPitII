import sqlite3
import pandas as pd

conn = sqlite3.connect('db/acoes.db')

query = "SELECT * FROM acoes"
df = pd.read_sql_query(query, conn)

conn.close()

print(df)