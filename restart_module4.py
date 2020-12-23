from urllib import request
from bs4 import BeautifulSoup

if __name__  == "__main__":
    soup = BeautifulSoup(urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20161120').read(), 'html.parser')
    res = soup.find_all('div', 'tit5')
 
    for n in res:
        print(n.get_text())