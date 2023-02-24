import polars as pl
import requests

#data = {"a": [1, 2], "b": [3, 4]}
#df = pl.DataFrame(data)
#print(df)

# Faz uma solicitação GET para a API
response = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-2019%27&@dataFinalCotacao=%2712-31-2025%27&$top=9000&$format=text/csv&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao")

# Extrai os dados da resposta como uma lista de dicionários
data = response.json()

# Cria um DataFrame Polars a partir dos dados extraídos
df = pl.DataFrame(data)

# Imprime o DataFrame
print(df)
