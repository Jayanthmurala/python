import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=iphones&crid=N6UKFD2IJPDI&sprefix=iphones%2Caps%2C215&ref=nb_sb_noss_2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    names = soup.find_all("span", attrs={"class": "a-size-medium a-color-base a-text-normal"})
    product_names = [name.get_text() for name in names[:20]]
    print(product_names)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
