import sqlite3
import pymongo
from pymongo import aggregation
import urllib

import json
class Database():
    mongo = pymongo.MongoClient("mongodb://localhost:27017/")
    #mongo = pymongo.MongoClient("mongodb://oddsing:"+urllib.parse.quote("!@%17aBc1212")+"@localhost:27017/")

    databaseM = mongo["oddsing"]
    collection = databaseM['odds']
    listaDeJogos = None
    def setCollection(self):
        self.collection = self.databaseM['odds']

    def insertDados(self, dados):
        self.dados = dados
        self.cur.execute("insert into jogo (tCasa,tFora,banca,odds) values (?, ?, ?, ?)", (self.dados['tCasa'], self.dados['tFora'], self.dados['banca'], str(self.dados['odds'])))
        self.con.commit()

    def insertMongo(self,dados):
        self.desativarAtivos(dados)
        result = self.collection.insert_one(dados)
        print('carregado: '+str(result.inserted_id))
        
    def desativarAtivos(self,dados):
        print(dados['sistema'])
        if dados['sistema'] == "kbets":
            result = self.collection.update_many({"ativo": True, "tCasaOriginal": dados['tCasaOriginal'], "tForaHoriginal":dados['tForaHoriginal'], 'banca': dados['banca']}, { "$set": {"ativo": False}})
        elif dados['sistema'] == "bolinha":
            result = self.collection.update_many({"ativo": True, "tCasaOriginal": dados['tCasaOriginal'], "tForaHoriginal":dados['tForaHoriginal'], 'banca': dados['banca']}, { "$set": {"ativo": False}})
            print(result.modified_count)
        else:
            result = self.collection.update_many({"ativo": True, "tCasa": dados['tCasa'], "tFora":dados['tFora'], 'banca': dados['banca']}, { "$set": {"ativo": False}})

    def getAllTimes(self):
        aggregate = [{"$match": { "ativo": True,  "sistema": "sa sports" } },{"$group" : { "_id": { "tCasa": "$tCasa", "tFora" : "$tFora"}} }]
        result = Database.mongo["oddsing"]["odds"].aggregate(aggregate)
        result = list(result)
        newResult = map( lambda x: x['_id'] ,result)
        self.listaDeJogos = newResult
        return list(newResult)
    def getBancasList(self, sistema):
        collection = self.databaseM['banca']
        result = collection.find({"rastrear": True, "sistema": sistema},{"_id":0,"url":1})
        result = list(map( lambda x : x['url'] , result))
        return result
    def getBancasListComplet(self, sistema):
        collection = self.databaseM['banca']
        result = collection.find({ "sistema": sistema, "imagem": {"$size" : 0}},{"_id":1,"url":1,"banca":1})
        return list(result)
    def setImageInBanca(self,id,url_base,size,banca):
        collection = self.databaseM['banca']
        result = collection.update_one({"_id": id}, { 
            "$push": {
                "imagem": { 
                    "size": size,
                    "url": url_base+"/"+banca+"/"+size+"/"+str(id)+".png"
                    }
                }
            }
        )
        print(result.modified_count)

