import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Year':2008, 'Age':19})

print(r.json())