import pandas as pd
df = pd.read_json("json\product\product-in-subImg\product-in-subImg-data.json")
print(len(df))
print(df.duplicated().sum())