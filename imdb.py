import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"
bas=requests.get(url)
html=bas.content

soup=BeautifulSoup(html,"html.parser")
ratings = soup.find_all("td",{"class","ratingColumn imdbRating"})

names=soup.find_all("td",{"class":"titleColumn"})

x=float(input("rating giriniz: "))


for name,rating in zip(names,ratings):
    rating=rating.text
    name=name.text

    rating=rating.strip()
    name=name.strip()

    rating=rating.replace("\n","")
    name=name.replace("\n","")

    if x<=float(rating):
        print("Film ismi :{},Film ratingi:{} ".format(name,rating))

