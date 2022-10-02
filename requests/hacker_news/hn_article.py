import requests
import json

# Вызов API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)

# Анализ структуры данных.
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
