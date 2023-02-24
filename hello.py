import requests
import polars as pl

print(pl.__version__)

response = requests.get('https://jsonplaceholder.typicode.com/todos')

data = response.json()


df = pl.DataFrame(data)

print(df)

df2 = df.drop("userId")

df2 = df2.with_column(pl.col('title','id','completed').cast(pl.Utf8))

def to_uppercase(s: str) -> str:
    return s.upper()

series = df2['title','id','completed'].apply(to_uppercase)

print(series)
