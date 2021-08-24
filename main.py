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
import threading
from database import Database
import traceback
import logging

import concurrent.futures

THREADS_N = 8
class CarregamentoDeLinks():
    def __init__(self):
        self.database =  Database()
        self.bancaListLink = None
        self.listLinkOdds  = None

    def ScrapingLinksKbets(self):
        self.linksK = self.database.getBancasList('kbets')
        for k in self.linksK:
            self.scrapingCompletoKbets(k)

    def scrapingCompletoKbets(self,link):
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS_N) as executor:
                instancia = scrapK(link)
                executor.map(self.scrapingOddsKbets,instancia.getAllId())
        except:
            traceback.print_exc()   
    
    def scrapingOddsKbets(self,item):
        #print('thread: ',threading.get_ident())
        result = scrapkbetsodds(item['link'], casa=item['gameItem'][0]['tc'], fora=item['gameItem'][0]['tf'],dateMatch=item['date_match']).Start()
        print(result)
        self.salve(result)

    def ScrapingOddSA(self):
        links = self.database.getBancasList('sa sports')
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
        with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS_N) as executor:
            executor.map(self.RasparMaisOddsSA,arr)
      

    def RasparMaisOddsSA(self,dados):
        print('thread: ',threading.get_ident())
        try:
            a = scrapsaodds(dados['link'],dados['date_match']).scrapCompleto()
            self.salve(a)
        except Exception:
            traceback.print_exc()    

    def ScrapingOddsBolinha(self):
        self.linksBolinha = self.database.getBancasList('bolinha')
        for i in self.linksBolinha:
            self.RasparOddsBolinhas(i)

    def RasparOddsBolinhas(self,link):
        link = scrapBol(link).getMainData()
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS_N) as executor:
                executor.map(self.ProcessarMultithreadBolinha,link)
        except:
            traceback.print_exc()
    
    def ProcessarMultithreadBolinha(self,i):
        print('thread: ',threading.get_ident())
        odds = scrapbolinhaodds(i['link'],i['date_match'],i['tCasa'],i['tFora'],i['camp_nome']).scrapCompleto()
        self.salve(odds)

    def salve(self,body):
        print('salve')
        self.database.insertMongo(body)

a = CarregamentoDeLinks()


while True:
    a.ScrapingOddSA()
    a.ScrapingLinksKbets()
    a.ScrapingOddsBolinha() 

""" while True:
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(a.ScrapingOddSA)
        executor.submit(a.ScrapingLinksKbets)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
        executor.submit(a.ScrapingOddsBolinha)
 """

