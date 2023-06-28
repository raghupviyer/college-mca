import requests

response = requests.get('https://www.example.com')

if response.status_code == 200:
  html_content = response.content
else:
  pass

html_content = response.content.decode('utf-8')
print(html_content)
print(response.status_code)
print(response.url)