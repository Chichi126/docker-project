import requests
from bs4 import BeautifulSoup
import time

page = requests.get("http://quotes.toscrape.com/")

soup = BeautifulSoup(page.text, "html.parser")

quotes = soup.find_all("span", attrs= {"class":"text"})
author = soup.find_all("small", attrs={"class", "author"})

for quotes, author in zip(quotes, author):
    print(quotes.text + "_" + author.text)
print("about to sleep")
time.sleep(10000)

