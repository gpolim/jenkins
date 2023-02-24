import polars as pl

print("Hello World")

data = {"a": [1, 2], "b": [3, 4]}
df = pl.DataFrame(data)
print(df)
