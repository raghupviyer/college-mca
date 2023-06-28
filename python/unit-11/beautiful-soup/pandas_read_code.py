import pandas as pd
colnames=['TITLE','TEACHER','DESCRIPTION', 'WATCH']


dataset = pd.read_csv("./data.csv", names=colnames, header=None, encoding='cp1252')
print(dataset)