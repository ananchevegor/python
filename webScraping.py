import requests
from bs4 import BeautifulSoup
import lxml
import requests
import csv
import sys
#

def write_page(url_link):
    url = url_link
    headers = {
        "accept": "*/*",
        "user - agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 98.0.4758.102Safari / 537.36"
    }
    req = requests.get(url, headers=headers)
    src = req.text
    with open("indexBinance.html", "w", encoding='utf-8') as file:
        file.write(src)


# write_page("https://www.binance.com/ru/markets")


def find_coin():
    with open("indexBinance.html", encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    coin = soup.find_all(class_="css-1wp9rgv")
    coin_price = soup.find_all(class_="css-ydcgk2")

    mas_coin_all = []
    mas_coin_price = []

    for item in coin_price:
         _coin_price_all = item.text
         mas_coin_price += _coin_price_all.split()
    for item in coin:
        coin_text_all = item.text
        mas_coin_all += coin_text_all.split()
    print(*mas_coin_all, sep=" ")
    print(*mas_coin_price, sep=" ")
    with open(f"/{mas_coin_all}_{mas_coin_price}.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                mas_coin_all,
                mas_coin_price
            )
        )




find_coin()

def search_class():
    with open("index.html", encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    vote = soup.find_all(class_="vote")
    seasons = soup.find_all(class_="season_pack")
    doctor = soup.find_all(class_="vote", string="Доктор Форман")
    print(doctor)
    for item in seasons:
        seson_text = item.text
        print(seson_text)
    all_votes = []
    for item in vote:
        item_text = item.text
        # print(item_text)
        all_votes = item_text
        print(all_votes)
# search_class()


