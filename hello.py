import requests
import polars as pl

print(pl.__version__)

response = requests.get('https://jsonplaceholder.typicode.com/todos')

data = response.json()


df = pl.DataFrame(data)

print(df)

df2 = df.drop("userId")

# Converta a coluna 'title' em um tipo de dados Utf8
df2 = df2.with_column(pl.col('title').cast(pl.Utf8))

# Defina uma função personalizada para converter a string em maiúsculas
def to_uppercase(s: str) -> str:
    return s.upper()

# Aplique a função personalizada à coluna 'title' usando o método 'apply()'
series = df2['title'].apply(to_uppercase)

# Crie uma nova coluna com os valores retornados pelo método 'apply()'


print(series)
