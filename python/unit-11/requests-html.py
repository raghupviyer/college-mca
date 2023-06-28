from requests_html import HTML, requests

response = requests.get('https://www.example.com')

html_content = None

if response.status_code == 200:
  html_content = response.content.decode('utf-8')
  # print("Connection Established with ressponse code", response.status_code)

else:
  print("The request was unsuccessful")
  pass

html = HTML(html = html_content)

links = html.find('a');
print(links)

for link in links:
  print(link.text)
  print(link.attrs['href'])
  print('--')
print('---')

divs = html.find('div')
for div in divs:
  print(div.text)
  print('--')
  print('\n')



# html_content = response.text

title = html.find('title', first=True).text
h1 = html.find('h1', first=True).text
div = html.find('div', first=True).text

print(title, h1, div)