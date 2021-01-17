import urllib.request as req
from bs4 import BeautifulSoup
import csv

def scrapeBalls(url):
  res = req.urlopen(url)
  hisp = BeautifulSoup(res,"html.parser")

  ballLinks = hisp.select(".woocommerce-LoopProduct-link")
  for link in ballLinks:
    getBallDetails(link.get("href"))

def getBallDetails(url):
  res = req.urlopen(url)
  ball = BeautifulSoup(res,"html.parser")
  name = ball.select_one(".product_title").string
  core = ball.select_one(".core > .attribute-value > a").string
  coverstock = ball.select_one(".coverstock > .attribute-value > a").string
  with open('C:\\Users\\miya7\\Desktop\\scraping\\hisp-balls\\ball-list.csv','a',encoding='utf8') as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerow([name,core,coverstock])
  f.close()

def main():
  url = "https://hi-sp.co.jp/product-category/ball/"
  pages = [url]
  for i in range(2,17):
    nextpage = url + "page/" + str(i) + "/"
    pages.append(nextpage)
  
  for page in pages:
    print(page)
    scrapeBalls(page)
  

if __name__ == "__main__":
  main()
