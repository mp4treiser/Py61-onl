import requests

api_key = "CG-LZLYTpfReraNvXY2hb8qX1fE"

# Task1
# Выполнено

# Task2
print("Task2")
""" Доступность API """
url = "https://api.coingecko.com/api/v3/ping"
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": api_key
}
response = requests.get(url, headers=headers)

print(f"Статус: {response.status_code}")

# Task3
print("\nTask3")
""" Парсинг монет, наименование которых включает ETH"""
url = "https://api.coingecko.com/api/v3/search?query=ETH"
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": api_key
}
response = requests.get(url, headers=headers)
print(response.text)

# Task4
print("\nTask4")
""" Трендовые монеты"""
url = "https://api.coingecko.com/api/v3/search/trending"
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": api_key
}
response = requests.get(url, headers=headers)
data = response.json()
coin_names = [coin["item"]["name"] for coin in data["coins"]]
print(coin_names)

# Task5
print("\nTask5")
""" Отправка заведомо неверного запроса для получения 404"""
url = "https://api.coingecko.com/api/v3/test"
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": api_key
}
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Сервер вернул {response.status_code}")
else:
    data = response.json()
    coin_names = [coin["item"]["name"] for coin in data["coins"]]
    print(coin_names)

# Task6
print("\nTask6")
""" Отправка POST запрсоа на публикацию поста в VK """
message = "Hello World!!"
token_vk = "vk1.a.R9Sjh__Lmfsp86_VdKsusFxMBoWf495vl_yOPWoTA83v73U47-5-a8u24RrYVt3lVABOgIjXqkeIJ5tHijCZli_3kZShG_6p-nLstl5iOe-h3RMLDEwmwosVAqMYZ1ktqFIRoCbOmEIElfARFzwHr4stci2loZ4a0fp7CgMds-pUelSgMx90FzMP_CqA4oBhDJ87xaR8Ce8mP9jaCCEkAg"
url = "https://api.vk.com/method/wall.post"
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
data = {
    "access_token": token_vk,
    "message": message,
    "v": "5.199"
}
response = requests.post(url=url, headers=headers, data=data)
print(f"https://vk.com/id813757194?w=wall813757194_{response.json()['response']['post_id']}")