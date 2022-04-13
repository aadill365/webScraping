from bs4 import BeautifulSoup
import requests,html5lib

class Scraper:
    def __init__(self):
        self.r = requests.get('https://theverge.com')
        self.soup = BeautifulSoup(self.r.content,'html5lib')

    def articles(self):
        table = self.soup.find('div')
        articles = table.findAll('div',attrs={'class':'c-entry-box--compact'})

        data = []
        
        for article in articles:
            article_data = {}
            #article_data['id'] = article.find('div',attrs={'data-chorus-optimize-module':'entry-box'})
            try:
                id= article.find('span',attrs={'class':"c-byline__gear"}).a['data-cdata']
                _,id=id.split(':')
                article_data['id']=int(id[:-1])
                
            except:
                article_data['id'] = None
            article_data['url']=article.h2.a['href']
            article_data['headline']=article.h2.text
            
            try:
                article_data['author']=article.find('span',attrs={'class':'c-byline__author-name'}).text
            except:
                article_data['author']='NA'
            try:
                
                 article_data['date'] =article.span.time['datetime']
            except:
                article_data['date'] = 'Not mentioned'
           
            article.span.time
            data.append(article_data)
        return data
