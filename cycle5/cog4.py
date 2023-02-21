import pandas as pd
df=pd.read_csv("studentdetails.csv")
#print(df)
spc=df["Student Name"]
#print(spc)
#print(df.head())
print(df.tail())

#print(df[["Student Name","Grade"]])
#print(df)