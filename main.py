#!/usr/bin/python3
from scrapingLinks import RaparLinksOddsSa as scrap
from scrapingLinks import RaparLinksOddsKbets as scrapK
from scrapingLinks import RaparLinksOddsBolinha as scrapBol
from scrapingOdds import RaparOddsSa as scrapsaodds
from scrapingOdds import rasparDadosKbets as scrapkbetsodds
from scrapingOdds import ScrapingOddsBolinha as scrapbolinhaodds
from database import Database
import traceback

class CarregamentoDeLinks():
    def __init__(self):
        self.database =  Database()
        self.links = self.database.getBancasList('sa sports')
        self.linksK = self.database.getBancasList('kbets')
        self.linksBolinha = self.database.getBancasList('bolinha')
        #self.bancaListLink = None
        #self.listLinkOdds  = None

    def ScrapingLinksKbets(self):
        for k in self.linksK:
            self.scrapingCompletoKbets(k)

    def scrapingCompletoKbets(self,link):
        try:
            self.scrapingOddsKbets(scrapK(link))
        except:
            traceback.print_exc()   
    
    def scrapingOddsKbets(self,instance):
        for item in instance.getAllId():
            result = scrapkbetsodds(item['link'], casa=item['gameItem'][0]['tc'], fora=item['gameItem'][0]['tf'],dateMatch=item['date_match']).Start()
            self.salve(result)

    def ScrapingOddSA(self):
        links = self.links
        for link in links:
            self.RaspagemCompletaLinkSA(link)

    def RaspagemCompletaLinkSA(self,link):
        arr = self.ScrapingLinkMainOddsSA(link)
        self.RasparTodosOsLinksMaisOddsSA(arr)
    
    def ScrapingLinkMainOddsSA(self,link):
        try:
            listLinksScraping = scrap(link).RaspagemCompleta()
        except:
            listLinksScraping = []
        return listLinksScraping

    def RasparTodosOsLinksMaisOddsSA(self,arr):
        for dados in arr:
            self.RasparMaisOddsSA(dados['link'],dados['date_match'])

    def RasparMaisOddsSA(self,link,date_match):
        try:
            a = scrapsaodds(link,date_match).scrapCompleto()
            self.salve(a)
        except Exception:
            traceback.print_exc()    

    def ScrapingOddsBolinha(self):
        for i in self.linksBolinha:
            self.RasparOddsBolinhas(i)

    def RasparOddsBolinhas(self,link):
        link = scrapBol(link).getMainData()
        for i in link:
            try:
                odds = scrapbolinhaodds(i['link'],i['date_match'],i['tCasa'],i['tFora'],i['camp_nome']).scrapCompleto()
                self.salve(odds)
            except:
                traceback.print_exc()

    def salve(self,body):
       self.database.insertMongo(body)

a = CarregamentoDeLinks()
data = Database()
for i in range(1,1000):
    a.ScrapingOddSA()
    a.ScrapingLinksKbets()
    a.ScrapingOddsBolinha()
