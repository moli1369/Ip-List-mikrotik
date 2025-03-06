import requests

url = 'https://raw.githubusercontent.com/moli1369/Ip-List-mikrotik/refs/heads/main/Iran-mikrotik'  # آدرس منبع IP
response = requests.get(url)
with open("ip-list.txt", "w") as file:
    file.write(response.text)
