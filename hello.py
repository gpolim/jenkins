import polars as pl
import requests

#data = {"a": [1, 2], "b": [3, 4]}
#df = pl.DataFrame(data)
#print(df)

# Faz uma solicitação GET para a API
response = requests.get('https://jsonplaceholder.typicode.com/todos')

# Extrai os dados da resposta como uma lista de dicionários
data = response.json()

# Cria um DataFrame Polars a partir dos dados extraídos
df = pl.DataFrame(data)

# Imprime o DataFrame
print(df)
