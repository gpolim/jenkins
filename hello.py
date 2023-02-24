import requests
import polars as pl

print(pl.__version__)

response = requests.get('https://jsonplaceholder.typicode.com/todos')

data = response.json()


df = pl.DataFrame(data)

print(df)

df2 = df.drop("userId")

df2 = df2.with_column(pl.col('title').cast(pl.Utf8))

# Converta o conteúdo da coluna 'title' em maiúsculas
df2['title'] = df2['title'].str_to_upper()

print(df2)
