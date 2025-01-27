import pandas as pd

df_csv = pd.read_csv('assignment_3_real/Iris.csv')
df_csv=df_csv.drop(4)
df_csv=df_csv.drop('PetalLengthCm',axis=1)
print(df_csv.head()) 