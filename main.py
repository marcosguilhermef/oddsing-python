#!/usr/bin/python3
from pymongo import database
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
        self.database =  Database()
        self.links = self.database.getBancasList('sa sports')
        self.linksK = self.database.getBancasList('kbets')
        self.bancaListLink = None
        self.listLinkOdds  = None
        
    def ScrapingLinksSA(self):
        newList = []
        for link in self.links:
            try:
                responseBody= scrap(link)
                listLinksScraping = list(map( lambda x: link +'/simulador'+ x, responseBody.Raspar()))
            except:
                listLinksScraping = []
            newList = newList + listLinksScraping
        self.listLinkOdds = Link(newList)
        return self.listLinkOdds

    def ScrapingLinksSARenew(self):
        newList = []
        for link in self.links:
            try:
                listLinksScraping = scrap(link).RaspagemCompleta()
            except:
                listLinksScraping = []
            newList = newList + listLinksScraping
        return newList

    def ScrapingLinksKbets(self):
        for k in self.linksK:
            self.scrapingOddsKbets(scrapK(k))

    def scrapingOddsKbets(self,instance):
        for item in instance.getAllId():
            result = scrapkbetsodds(item['link'], casa=item['gameItem'][0]['tc'], fora=item['gameItem'][0]['tf'],dateMatch=item['gameItem'][0]['data_hora']).Start()
            self.salve(result)

    def ScrapingOddSA(self):
        linkOdds = self.ScrapingLinksSARenew()
        for info in linkOdds:
            try:
                a = scrapsaodds(info['link'],info['date_match']).scrapCompleto()
                self.salve(a)
            except:
                print('pula')   
    
    def salve(self,body):
       print('salvando')
       self.database.insertMongo(body)

a = CarregamentoDeLinks()
data = Database()
a.ScrapingOddSA()
a.ScrapingLinksKbets()
