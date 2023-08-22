import pandas as p

p.Series([])
p.DataFrame([])
data = p.read_csv('something.csv')
data.head() #first 5 rows
data.head(n) #first n rows
data.tail() #last 5 rows
data.tail(n) #last n rows