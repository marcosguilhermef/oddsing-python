#!/usr/bin/python3
from pymongo import database

from scrapingLinks import RaparLinksOddsSa as scrap
from scrapingLinks import RaparLinksOddsKbets as scrapK
from scrapingLinks import RaparLinksOddsBolinha as scrapBol


from datasets import Link

from lerArquivoDeLinks import ArquivoSA as lerSa
from lerArquivoDeLinks import ArquivoKBETS as lerK

from connect import ConectSA

from scrapingOdds import RaparOddsSa as scrapsaodds
from scrapingOdds import rasparDadosKbets as scrapkbetsodds
from scrapingOdds import ScrapingOddsBolinha as scrapbolinhaodds

from SalvarEmTexto import SalvarArquivoTexto as save
from threading import Thread
from database import Database
import traceback

class CarregamentoDeLinks():
    def __init__(self):
        self.database =  Database()
        self.links = self.database.getBancasList('sa sports')
        self.linksK = self.database.getBancasList('kbets')
        self.linksBolinha = self.database.getBancasList('bolinha')
        self.bancaListLink = None
        self.listLinkOdds  = None
        
    

    def ScrapingLinksKbets(self):
        for k in self.linksK:
            try:
                self.scrapingOddsKbets(scrapK(k))
            except:
                pass

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
                print('erro')

    
    def salve(self,body):
       print('salvando')
       self.database.insertMongo(body)

a = CarregamentoDeLinks()
data = Database()
for i in range(1,1000):
    a.ScrapingOddSA()
    a.ScrapingLinksKbets()
    a.ScrapingOddsBolinha()
a.RaspagemCompletaLinkSA('betscash.net')

#a.RasparOddsBolinhas("esportenetvip.com.br")
