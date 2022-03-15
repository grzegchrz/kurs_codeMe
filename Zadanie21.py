import pandas as pd

df=pd.read_csv('przewoz_osob_gdynia.csv')

q = df.max()
p = df.min()
print(f"Data wartości maksymalnej: {q[1]}")
print(f"Data wartości minimalnej: {p[1]}")
