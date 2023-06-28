from bs4 import BeautifulSoup
import requests
import re
import csv

response = requests.get('https://bombaybiblecollege.com/allcourses')

html = BeautifulSoup(response.content, 'html.parser')

header = html.find('header', id='top')
lines = html.find_all('a', class_="text-indigo-500 inline-flex items-center md:mb-2 lg:mb-0")

for line in lines:
  print(line)
  print('-')
  print(line.text)
  print('---')

h3 = html.find_all("h3")
print(h3)


for line in h3:
 print(line.text)

print('---courses---')

courses = html.find_all('div', class_="p-4 md:w-1/3")

data=[]
for course in courses:
  data.append(re.split('[\n]+', course.get_text().strip()))

for i in enumerate(data):
  print('---')
  print(i[0])
  for j in enumerate(i[1]):
    print(j[1])
    row = i[0]
    col = j[0]
    data[row][col] = j[1]

print(data)

with open('data.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(data)