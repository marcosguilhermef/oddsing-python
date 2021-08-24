import traceback
from warnings import catch_warnings, simplefilter
import connect
from bs4 import BeautifulSoup
import re
import json  
import datetime
import database
from OddParametrizacao import bolinhaParaSa
from OddParametrizacao import kbetsParaSa

from difflib import SequenceMatcher

class RaparOddsSa():
    def __init__(self,link,dateMatch = ''):
        self.link = link
        self.Request()
        self.StartSoup()
        self.oddsJSON = {}
        self.oddsJSON['data_hora'] = datetime.datetime.now()
        self.oddsJSON['sistema'] = 'sa sports'
        self.oddsJSON['date_match'] = dateMatch

       
    def Request(self):
        self.body = connect.ConectSA(self.link).getBody()
        
    def StartSoup(self):
        self.soup  = BeautifulSoup(self.body, 'html.parser')

    def scrapCasaFora(self):
        self.CasaFora = self.soup.find(id='conteudo_tituloCampeonato')
        self.CasaFora = re.sub('Apostas Disponíveis - ','',self.CasaFora.text)
        splod = re.split('x',self.CasaFora)
        self.oddsJSON['tCasa'] = re.sub('(\s)$|^(\s)','',splod[0])
        self.oddsJSON['tFora'] = re.sub('(\s)$|^(\s)','',splod[1])
        return self.CasaFora
    
    def scrapOdds(self):
        #print(self.body)
        tipoDeOdd = None
        self.oddsSoap = self.soup.find_all('tr', limit=False)
        self.oddsJSON['odds'] = []
        for odd in self.oddsSoap:
            td = odd.find_all('td')
            try:
                text = td[1].get_text()
                parametrizar =  { "nome":td[0].get_text(),"Taxa": float(text.replace(',','.') if text != '' else '0') , "tipo": tipoDeOdd} 
                self.oddsJSON['odds'].append(parametrizar)
            except IndexError:
                if len(td) != 0:
                    tipoDeOdd = td[0].get_text()
            
        

        return self.oddsJSON 
        #json.dumps(self.oddsJSON, indent = 4) 
    def scrapNomeBanca(self):
        self.oddsJSON['banca'] = re.search('\w{1,}', self.link).group(0)
        print(self.oddsJSON['banca'])
       

    def setStatus(self):
        self.oddsJSON['ativo'] = True 

    def scrapCompleto(self):
        self.scrapNomeBanca()
        self.scrapCasaFora()
        self.scrapOdds()
        self.setStatus()
        return self.getOddsJSON()

    def getOddsJSON(self):
        return self.oddsJSON

class rasparDadosKbets():
    listaDeJogos = None
    def __init__(self,link,casa= '',fora = '', dateMatch= None):
        self.link = link
        self.casa = casa
        self.fora = fora
        self.Request()
        self.oddsJSON = {}
        self.oddsJSON['sistema'] = 'kbets'
        self.oddsJSON['date_match'] = dateMatch


    def Request(self):
        try:
            self.body = connect.ConectKbets(self.link+'/axios/data').getBody()
        except Exception as e:
            raise e
    
    def Start(self):
        self.setBanca()
        self.setHora()
        self.setStats()
        self.setCasaFora()
        self.oddsJSON['odds'] = self.setOdds()
        return self.oddsJSON
    def setBanca(self):
        self.oddsJSON['banca'] = re.search('\w{1,}', self.link).group(0)

    def setHora(self):
        self.oddsJSON['data_hora'] = datetime.datetime.now()
    def setStats(self):
        self.oddsJSON['ativo'] = True

    def setCasaFora(self):
        self.gerarNome()
        NomesSubstituiveis = self.obterNomeCasaNomeFora(self.casa, self.fora)
        self.oddsJSON['tCasa'] = NomesSubstituiveis['casa']
        self.oddsJSON['tFora'] = NomesSubstituiveis['fora']
        self.oddsJSON['tCasaOriginal'] = self.casa
        self.oddsJSON['tForaHoriginal'] = self.fora
    def gerarNome(self):
        db = database.Database()
        lista = db.getAllTimes()
        self.listaSAgames = lista
    def obterNomeCasaNomeFora(self, casa,fora):
        listaSAgames = self.listaSAgames
        casaResult = list(filter(lambda x: SequenceMatcher(None,x['tCasa'],casa).ratio() > 0.70 ,listaSAgames))
        if len(casaResult) == 0:
            casaResult = casa
        else:
            casaResult =casaResult[0]['tCasa']
            print('ratio: ',SequenceMatcher(None,casaResult,casa).ratio()," casa: "+casaResult," casa2: ", casa)

        foraResult = list(filter(lambda x: SequenceMatcher(None,x['tFora'],fora).ratio() > 0.70,listaSAgames))
        if len(foraResult) == 0:
            foraResult = fora
        else:
            foraResult = foraResult[0]['tFora']
            print('ratio: ',SequenceMatcher(None,foraResult,fora).ratio()," fora: "+foraResult," fora2: ", fora)
        return { "casa": casaResult, "fora": foraResult }

    def setOdds(self): 
        self.oddsJSON['odds'] = []
        for x in self.body:
            try:
                compatibilizar = kbetsParaSa(x["grupo_id"],x['odds'],x['grupo'])
                grupo = compatibilizar.getGrupoOdd()
                oddsNome = compatibilizar.getName()
                odd = { "tipo": grupo, "Taxa": float(x["taxa"]), "nome": oddsNome }
                self.oddsJSON['odds'].append(odd)
            except:
                traceback.print_exc()
                exit()
        return self.oddsJSON['odds']

class ScrapingOddsBolinha():
    def __init__(self,link, date_match,tCasa = '',tFora = '',campeonato = ''):
        self.link = link
        self.Request()
        
        self.oddsJSON = {}
        self.oddsJSON['data_hora'] = datetime.datetime.now()
        self.oddsJSON['sistema'] = 'bolinha'
        self.oddsJSON['tCasa'] = tCasa
        self.oddsJSON['tFora'] = tFora
        self.oddsJSON['tCasaOriginal'] = tCasa
        self.oddsJSON['tForaHoriginal'] =tFora
        self.oddsJSON['visivel'] = True
        self.oddsJSON['ativo'] = True
        self.oddsJSON['banca'] = re.search('\w{1,}', self.link).group(0)
        self.oddsJSON['date_match'] = date_match
        self.oddsJSON['campeonato'] = campeonato

        self.mudarNome()


    def Request(self):
        try:
            self.body = connect.ConectBolinha(self.link).getBody()
            self.body = re.sub("'{","{",str(self.body))
            self.body = re.sub("}'",'}',str(self.body))
            self.body = re.sub("'","\"",self.body)
            self.body = json.loads(self.body)
        except Exception as e:
            raise e

    def getBody(self):
        return self.body[0]
    def mudarNome(self):
        db = database.Database()
        lista = db.getAllTimes()
        self.listaSAgames = lista

        novoNome = self.obterNomeCasaNomeFora(self.oddsJSON['tCasa'],self.oddsJSON['tFora'])
        self.oddsJSON['tCasa'] = novoNome['casa']
        self.oddsJSON['tFora'] = novoNome['fora']

    def scrapCompleto(self):
        self.scrapOdds()
        return self.oddsJSON

    def scrapOdds(self):
        self.oddsJSON['odds'] = []
        for i in self.body:
            compatibilizar = bolinhaParaSa(i['Value']['cat_id'],i['Value']['descricao'])
            odd_dados = { 'nome': compatibilizar.getName(),'Taxa': i['Value']['taxa'] ,'tipo': compatibilizar.getGrupoOdd() }
            self.oddsJSON['odds'].append(odd_dados)
    
    def obterNomeCasaNomeFora(self, casa,fora):
        listaSAgames = self.listaSAgames
        casaResult = list(filter(lambda x: SequenceMatcher(None,x['tCasa'],casa).ratio() > 0.70 ,listaSAgames))
        if len(casaResult) == 0:
            casaResult = casa
        else:
            casaResult =casaResult[0]['tCasa']
            print('ratio: ',SequenceMatcher(None,casaResult,casa).ratio()," casa: "+casaResult," casa2: ", casa)

        foraResult = list(filter(lambda x: SequenceMatcher(None,x['tFora'],fora).ratio() > 0.70,listaSAgames))
        if len(foraResult) == 0:
            foraResult = fora
        else:
            foraResult = foraResult[0]['tFora']
            print('ratio: ',SequenceMatcher(None,foraResult,fora).ratio()," fora: "+foraResult," fora2: ", fora)
        return { "casa": casaResult, "fora": foraResult }
