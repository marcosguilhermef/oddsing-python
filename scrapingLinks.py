from warnings import catch_warnings
import connect
from bs4 import BeautifulSoup
import re

class RaparLinksOddsSa():
    def __init__(self,link):
        self.link = link
        self.body = self.getLinksMaisOdds()
    
    def getLinksMaisOdds(self):
        return connect.ConectSA(self.link).getBody()

    def Raspar(self):
        soup = BeautifulSoup(self.body, 'html.parser')
        #tr = soup.find_all('tr',limit=False)
        a = soup.find_all('a')
        links = map(lambda re : re['href'], a)
        linksTratados = map(lambda link: re.sub('(./)','/',link),links)
        linksUteis = map(lambda link:  link if re.search('javascript',link) == None else None ,linksTratados)
        linksUteisSemNones = self.removeNone(linksUteis)
        return linksUteisSemNones

    def removeNone(self, link):
        newList = []
        for i in link:
            if i != None:
                newList.append(i)
        return newList
