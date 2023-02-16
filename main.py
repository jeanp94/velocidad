import requests
url = 'mariaalmenara.pe'
response = requests.get(url)
response_time = response.elapsed.total_seconds()
print(f'Tiempo de respuesta: {response_time} segundos')
