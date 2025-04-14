#https://jsonplaceholder.typicode.com/
import requests
url='https://jsonplaceholder.typicode.com/photos/'
response=requests.get(url)
if response.status_code == 200:
    print('information get')
    print(response.json())
else: print("ERROR") 
#head
url1='http://testphp.vulnweb.com/'   
response=requests.head(url1)
print("information")
for k,v in response.headers.items():
    print(f'{k}:{v}')