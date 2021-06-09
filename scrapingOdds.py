from warnings import catch_warnings, simplefilter
import connect
from bs4 import BeautifulSoup
import re
import json  
import datetime
import database
from difflib import SequenceMatcher

class RaparOddsSa():
    def __init__(self,link):
        self.link = link
        self.Request()
        self.StartSoup()
        self.oddsJSON = {}
        self.oddsJSON['data_hora'] = datetime.datetime.now()
        self.oddsJSON['sistema'] = 'sa sports'

       
    def Request(self):
        self.body = connect.ConectSA(self.link).getBody()
        
    def StartSoup(self):
        self.soup  = BeautifulSoup(self.body, 'html.parser')

    def scrapCasaFora(self):
        self.CasaFora = self.soup.find(id='conteudo_tituloCampeonato')
        self.CasaFora = re.sub('Apostas Disponíveis - ','',self.CasaFora.text)
        splod = re.split('x',self.CasaFora)
        self.oddsJSON['tCasa'] = splod[0]
        self.oddsJSON['tFora'] = splod[1]
        return self.CasaFora
    def scrapOdds(self):
        #print(self.body)
        tipoDeOdd = None
        self.oddsSoap = self.soup.find_all('tr', limit=False)
        self.oddsJSON['odds'] = []
        for odd in self.oddsSoap:
            td = odd.find_all('td')
            try:
                parametrizar =  { "nome":td[0].get_text(),"Taxa":td[1].get_text(), "tipo": tipoDeOdd} 
                self.oddsJSON['odds'].append(parametrizar)
            except IndexError:
                if len(td) != 0:
                    tipoDeOdd = td[0].get_text()
            
        

        return self.oddsJSON 
        #json.dumps(self.oddsJSON, indent = 4) 
    def scrapNomeBanca(self):
        self.oddsJSON['banca'] = re.search('(?<=https://)\w{1,}|(?<=http://)\w{1,}', self.link).group(0)
        
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
    def __init__(self,link,casa= '',fora = ''):
        self.link = link
        self.casa = casa
        self.fora = fora
        self.Request()
        self.oddsJSON = {}
        self.oddsJSON['sistema'] = 'kbets'

        
       
    def Request(self):
        self.body = connect.ConectKbets(self.link).getBody()
    
    def Start(self):
        self.setBanca()
        self.setHora()
        self.setStats()
        self.setCasaFora()
        self.setOdds()
        return self.oddsJSON
    def setBanca(self):
        self.oddsJSON['banca'] = re.search('(?<=https://)\w{1,}|(?<=http://)\w{1,}', self.link).group(0)

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
        self.oddsJSON['odds'] = list(map( lambda x : { "tipo": x["grupo"], "taxa": x["taxa"], "nome": x["odds"] } , self.body))
