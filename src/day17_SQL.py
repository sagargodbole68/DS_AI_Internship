import pandas as pd
import sqlite3
conn = sqlite3.connect("C:/DS_AI_Internship/data/internship.db")
df=pd.read_sql_query("SELECT name, track FROM interns", conn)
print(df)