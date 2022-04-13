import sys
import csv
import datetime
from scrape import Scraper
from config import Database

fields = ['id','url','headline','author','date']

try:
    sc = Scraper()
    data = sc.articles()
    
except:
    print('Please connect to your internet.')
    sys.exit()

date = datetime.datetime.now()
date = date.strftime("%d-%m-%y_verge.csv")

with open(date,'w') as f:
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

db = Database()

for article in data:
    if article['id'] is not None:
        db.insert(article['id'],article['url'],article['headline'],article['author'],article['date'])
        
res = db.select()
print(res)

