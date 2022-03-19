import pandas as pd

df=pd.read_csv('przewoz_osob_gdynia.csv')


i = df['tys_osob'].idxmax()

dateOfMax = (df['month'][i])

j = df['tys_osob'].idxmin()

dateOfMin = (df['month'][j])

print(f"Data wartości maksymalnej: {dateOfMax}")
print(f"Data wartości minimalnej: {dateOfMin}")
