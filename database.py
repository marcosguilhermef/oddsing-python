import sqlite3
import pymongo
from pymongo import aggregation
import json
class Database():
    mongo = pymongo.MongoClient("mongodb://localhost:27017/")
    databaseM = mongo["oddsing"]
    collection = databaseM['odds']
    listaDeJogos = None
    def setCollection(self):
        self.collection = self.databaseM['odds']
    def insertDados(self, dados):
        self.desativarAtivos()
        self.dados = dados
        self.cur.execute("insert into jogo (tCasa,tFora,banca,odds) values (?, ?, ?, ?)", (self.dados['tCasa'], self.dados['tFora'], self.dados['banca'], str(self.dados['odds'])))
        self.con.commit()
    def insertMongo(self,dados):
        result = self.collection.insert_one(dados)
        print('carregado: '+str(result.inserted_id))
    def desativarAtivos(self):
        self.collection.update_many({"ativo": True}, { "$set": {"ativo": False}})
    def getAllTimes(self):
        aggregate = [{"$match": { "ativo": True,  "sistema": "sa sports" } },{"$group" : { "_id": { "tCasa": "$tCasa", "tFora" : "$tFora"}} }]
        result = Database.mongo["oddsing"]["odds"].aggregate(aggregate)
        result = list(result)
        newResult = map( lambda x: x['_id'] ,result)
        self.listaDeJogos = newResult
        return list(newResult)