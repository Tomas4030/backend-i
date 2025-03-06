import requests

URLS =  "https://www.google.pt/?hl=pt-PT"
teste = requests.get(URLS)

print(URLS)

if teste:
    print("TA ligado pa")
else:
    print("FF n esta ligado")