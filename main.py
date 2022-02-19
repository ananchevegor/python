from bs4 import BeautifulSoup
import requests
from lxml import etree
import lxml.html
import csv


def parse(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    the_vote = tree.xpath('//*[@id="dle-vote"]/div[1]/text()')
    print(the_vote)


def main():
    parse("http://dh-online.ru/sezon-6/130-6-sezon-18-seriya-pavshiy-rycar.html")


if __name__ == "__main__":
    main()

def idk():
    url_html = "http://dh-online.ru/sezon-6/130-6-sezon-18-seriya-pavshiy-rycar.html"
    with open('url_html', 'r') as html_file:
        content = html_file.read()

        soap = BeautifulSoup

        print(content)
