import sqlite3

import pandas as pd

conn = sqlite3.connect("churn.db")

df = pd.read_csv("data/processed/churn_clean.csv")

df.to_sql("customers", conn, if_exists="replace", index=False)

print("Dados inseridos com sucesso!")

conn.close()
