import pandas as pd

df = pd.read_csv('file.csv')
pd.DataFrame(df).to_csv("final.csv")