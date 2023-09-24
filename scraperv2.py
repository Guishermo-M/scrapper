import requests

r=requests.options('https://www.instagram.com/')
print(r.text)


with open('caca.txt', 'w') as f:
    f.write(r.text)