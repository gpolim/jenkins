import requests
import polars as pl

response = requests.get('https://jsonplaceholder.typicode.com/todos')

data = response.json()


df = pl.DataFrame(data)

print(df)

df2 = df.drop("userId")
df2 = to_uppercase(df2)
print(df2)
