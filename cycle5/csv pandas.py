import pandas as pd
#df=pd.read_csv("studentdetail.csv")
#print("The data frame is:\n",df)
#print(df.head())
#specific_column=df[["name","roll no"]]
#print(specific_column)
#print(df.head())
#print(df.tail())
df=pd.read_csv("studentdetail.csv",usecols=["roll no","name","class"])
print(df)
