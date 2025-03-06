import requests

url = 'https://lite.ip2location.com/iran-(islamic-republic-of)-ip-address-ranges?lang=en_US'  # آدرس منبع IP
response = requests.get(url)
with open("ip-list.txt", "w") as file:
    file.write(response.text)
