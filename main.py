import requests
import time
import os

url = os.environ['URL']
start_time = time.time()
response = requests.get(url)
end_time = time.time()

load_time = end_time - start_time
print(f"Load time for {url}: {load_time:.2f} seconds")
