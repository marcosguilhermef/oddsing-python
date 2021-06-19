from os import link, stat
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
        linksUteis = map(lambda link:  link if re.search('apostas.aspx',link) != None else None ,linksTratados)
        linksUteisSemNones = self.removeNone(linksUteis)
        return linksUteisSemNones
    
    def removeNone(self, link):
        newList = []
        for i in link:
            if i != None:
                newList.append(i)
        return newList
        
#a = RaparLinksOddsSa("https://nbet91.com/simulador/jogos.aspx?idesporte=102&idcampeonato=575067")

class RaparLinksOddsKbets():
    def __init__(self,link):
        self.link = link
        self.oddsJSON = {}
        self.Request()
        self.Start()
       
    def Request(self):
        self.body = connect.ConectKbets(self.link+'/axios/data').getBody()
        
    def Start(self):
        self.oddsGroups = self.body['odds']
        self.gameList = self.body['lista']

    def getAllId(self):
        newArr = []
        for item in self.gameList:
            newArr.append({"link":"http://bestgameonline.net/axios/oddsWithGroups/"+item['id'], "id":item['id'], "gameItem": list(filter( lambda x : x['id'] == item['id'] ,self.gameList)) })
        return newArr

    def getOddsGroups(self):
        return self.oddsGroups

    def getgameList(self):
        return self.gameList
    
    