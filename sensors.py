import requests
import random
import time

url = 'http://localhost:5000/update'

while True:
    data = {
        "temperature": round(random.uniform(15, 25), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "pressure": round(random.uniform(1000, 1020), 2)
    }
    response = requests.post(url, json=data)
    print(f"Sent data: {data}, Response: {response.status_code}")
    time.sleep(5) # Відправляємо дані кожні 5 секунд
