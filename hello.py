import requests
import polars as pl

# Faz uma solicitação GET para a API
response = requests.get('https://jsonplaceholder.typicode.com/todos')

# Extrai os dados da resposta como uma lista de dicionários
data = response.json()

# Cria um DataFrame Polars a partir dos dados extraídos
df = pl.DataFrame(data)

# Imprime o DataFrame
print(df)
