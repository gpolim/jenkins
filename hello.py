import requests
import polars as pl

response = requests.get('https://jsonplaceholder.typicode.com/todos')

data = response.json()


df = pl.DataFrame(data)

print(df)

df2 = df.drop("userId")

df2['title'] = df2['title'].str_to_upper()

print(df2)
