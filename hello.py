import polars as pl
import requests

#data = {"a": [1, 2], "b": [3, 4]}
#df = pl.DataFrame(data)
#print(df)

# Faz uma solicitação GET para a API
api = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo"

# Extrai os dados da resposta como uma lista de dicionários
data = pl.read_csv(api)

# Cria um DataFrame Polars a partir dos dados extraídos
df = pl.DataFrame(data)

# Imprime o DataFrame
print(df)
