
import pandas  as pd

print(pl.__version__)

response = requests.get('https://jsonplaceholder.typicode.com/todos')

data = response.json()


df = pl.DataFrame(data)

print(df)
