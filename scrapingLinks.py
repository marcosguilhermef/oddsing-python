from os import link, stat
from warnings import catch_warnings
import connect
from bs4 import BeautifulSoup
import re
import datetime
class RaparLinksOddsSa():
    def __init__(self,link):
        self.link = link
        self.body = self.getLinksMaisOdds()
        self.pais = None,
        self.campeonato = None
        self.dataMatch = None
    
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
    def RaspagemCompleta(self):
        soup = BeautifulSoup(self.body, 'html.parser')
        a = soup.find_all('tr',limit=False) 
        informacoesIteis = []
        i = 0
        for e in a:
            try:
                if 'tcpais' in e.td['class']:
                    self.rasparPais(e.td.span.span.next_sibling.get_text())
                if 'tccampeonato' in e.td['class']:
                    self.rasparCampeonato(e.td.span.extract())
                if 'th_1' in e.td['class']:
                    date_match = e.td.p.next_sibling.get_text()
                    link = self.RasparLink(e)
                    link = re.sub('(./)','/',link)
                    informacoesIteis.append({
                        'campeonato': self.campeonato,
                        'pais': self.pais,
                        'date_match': datetime.datetime.strptime(date_match+" -03:00", '%d/%m/%Y %H:%M %z'),
                        'link': self.link+'/simulador'+link
                    })
            except:
                pass
        return informacoesIteis
    def rasparPais(self,pais):
        self.pais = pais.replace(u'\xa0', u' ')
    def rasparCampeonato(self,campeonato):
        self.campeonato = campeonato.get_text()
    def rasparDataMatch(self,dataMatch):
        self.dataMatch = dataMatch
    def RasparLink(self,raw):
        return raw.td.find_next_sibling(name="td", attrs={ 'class': 'th_5' }).a['href']

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
            newArr.append(
                {
                    "link":self.link+"/axios/oddsWithGroups/"+item['id'], 
                    "id": item['id'], 
                    "gameItem": list(filter( lambda x : x['id'] == item['id'] ,self.gameList)),
                    "date_match": datetime.datetime.strptime(item['data_hora']+" -03:00", '%Y-%m-%d %H:%M:%S %z')
                }
            )
        return newArr

    def getOddsGroups(self):
        return self.oddsGroups

    def getgameList(self):
        return self.gameList
    
#teste = print(RaparLinksOddsSa('https://betscash.net').RaspagemCompleta())