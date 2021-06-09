import pandas as pd
import json
import csv
import xml.etree.cElementTree as e


class SalvarArquivoTexto():
    
    def __init__(self, arquivo):
        self.arquivo = arquivo
        #self.setHeads()
        
    def save(self):
       arq = open('teste.json','a+')
       arq.write(json.dumps(self.arquivo))
    def getHeads(self):
        return self.heads
    
    def setHeads(self):
        self.heads = list(self.arquivo.keys())

    def csvsave(self):
        heads = self.getHeads()
        odds = self.arquivo
        print(json.dumps(odds))
    def htmlCreacre():
        table = '<table>'
class html():
    @staticmethod
    def setTable(corpo):
        return '<table>'+corpo+'</table>'
    @staticmethod
    def setBodyArray(array):
        string = ''
        for arr in array:
            pass