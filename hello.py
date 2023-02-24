import requests
import polars as pl

# Faz uma solicitação GET para a API
response = requests.get('https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo')

# Extrai os dados da resposta como uma lista de dicionários
data = response.json()

# Cria um DataFrame Polars a partir dos dados extraídos
df = pl.DataFrame(data)

# Imprime o DataFrame
print(df)
