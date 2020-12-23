import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.daangn.com/hot_articles") #당근마켓 인기매물 검색
print(webpage.text)

webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")

print(soup.p)
print(soup.p.string)
print(soup.h1)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

