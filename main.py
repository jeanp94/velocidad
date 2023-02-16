import requests
response = requests.get('mariaalmenara.pe')
response_time = response.elapsed.total_seconds()
print(f'Tiempo de respuesta: {response_time} segundos')
