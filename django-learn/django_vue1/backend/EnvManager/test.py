import requests
res=requests.get('http://localhost:8000/api/environment/')
print(res.content)
