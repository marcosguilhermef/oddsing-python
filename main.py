from pymongo import database
import datasets
from scrapingLinks import RaparLinksOddsSa as scrap
from scrapingLinks import RaparLinksOddsKbets as scrapK

from datasets import Link
from lerArquivoDeLinks import ArquivoSA as lerSa
from lerArquivoDeLinks import ArquivoKBETS as lerK
from connect import ConectSA
from scrapingOdds import RaparOddsSa as scrapsaodds
from scrapingOdds import rasparDadosKbets as scrapkbetsodds

from SalvarEmTexto import SalvarArquivoTexto as save
from threading import Thread
from database import Database

class CarregamentoDeLinks():
    def __init__(self):
        self.links = self.carregamentoSa()
        self.linksK = self.carregamentoLbets()
        self.bancaListLink = None
        self.listLinkOdds  = None
        self.database =  Database()
    def carregamentoSa(self):
        links = lerSa().ler()
        bancaListLink = Link(links)
        self.bancaListLink = bancaListLink.getLinkList()
        return self.bancaListLink

    def carregamentoLbets(self):
        links = lerK().ler()
        bancaListLink = Link(links)
        self.bancaListLink = bancaListLink.getLinkList()
        return self.bancaListLink

    def ScrapingLinksSA(self):
        newList = []
        for link in self.links:
            try:
                responseBody= scrap(link)
                listLinksScraping = list(map( lambda x: link +'/simulador'+ x, responseBody.Raspar()))
            except:
                print('pula')
            newList = newList + listLinksScraping
        self.listLinkOdds = Link(newList)
        return self.listLinkOdds
    def ScrapingLinksKbets(self):
        for k in self.linksK:
            self.scrapingOddsKbets(scrapK(k))

    def scrapingOddsKbets(self,instance):
        for item in instance.getAllId():
            result = scrapkbetsodds(item['link'], casa=item['gameItem'][0]['tc'], fora=item['gameItem'][0]['tf']).Start()
            self.salve(result)

    def ScrapingOddSA(self):
        linkOdds = self.ScrapingLinksSA()
        linkOdds = list(linkOdds.getLinkList())
        arrReturning = []
        for link in linkOdds:
            try:
                a = scrapsaodds(link).scrapCompleto()
                self.salve(a)
            except:
                print('pula')
        #self.salve(arrReturning)
    """ def ScrapingOddKbet(self):
        linkOdds = self.ScrapingLinksSA()
        linkOdds = list(linkOdds.getLinkList())
        for link in linkOdds:
            a = scrapsaodds(link).scrapCompleto()
            arrReturning.append(a)
            self.salve(a)
            try:
                pass
            except:
                print('pula') """
        #self.salve(arrReturning)
    def salve(self,body):
       print('salvando')
       self.database.insertMongo(body)
       #self.database.insertMongo(body)

a = CarregamentoDeLinks()
data = Database().desativarAtivos()
a.ScrapingOddSA()
a.ScrapingLinksKbets()
