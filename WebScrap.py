import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

response = requests.get('https://books.toscrape.com/',headers = headers)

print(response.status_code) # status code = 200
print(response.headers) # headers = {'content-type': 'application/json; charset=utf-8'}
if response.ok:
    print(response.text) # response.json() = {'message': 'Hello, World!
    
else:
    print('Could not connect to the website at http://toscrape.com - please try again')

