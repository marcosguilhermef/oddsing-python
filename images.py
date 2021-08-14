import requests
from bs4 import BeautifulSoup
import traceback
import pymongo
from pymongo import aggregation
from database import Database
import os
from PIL import Image
import io

class conectar:
    def __init__(self,link):
        self.link   = link
    def iniciar(self):
        try:
            r = requests.get('https://'+self.link)
            return r
        except:
            pass

DATABASE = Database()

PATH="imagens/"
URL_BASE="localhost/origin/imagem"
def salvarOriginal(link,id,img,banca,imgBruto):
    try:
        imgBrutoResize = Image.open(io.BytesIO(imgBruto))
        try:
            imgBrutoResize.save(PATH+banca+"/original/"+str(id)+'.png')
        except FileNotFoundError:
            os.mkdir(PATH+banca)
            imgBrutoResize.save(PATH+banca+"/original/"+str(id)+'.png')
        DATABASE.setImageInBanca(id,URL_BASE,'original',banca)
    except FileNotFoundError:
        os.mkdir(PATH+banca+"/original/")
        salvarOriginal(link,id,img,banca,imgBruto)

def salvar50por50(link,id,img,banca,imgBruto):
    try:
        imgBrutoResize = Image.open(io.BytesIO(imgBruto)).resize((50,50))
        try:
            imgBrutoResize.save(PATH+banca+"/50x50/"+str(id)+'.png')
        except FileNotFoundError:
            os.mkdir(PATH+banca)
            imgBrutoResize.save(PATH+banca+"/50x50/"+str(id)+'.png')
        DATABASE.setImageInBanca(id,URL_BASE,'50x50',banca)
    except FileNotFoundError:
        os.mkdir(PATH+banca+"/50x50/")
        salvar50por50(link,id,img,banca,imgBruto)


  
   
myresult = [{"_id":"60e464eb29bbaf27ded27cd3","banca":"bbsports","url":"bbsports.top","sistema":"sa sports","instagram":[],"telefone":[],"localizacao":[],"imagem":[],"rastrear":False,"visivel":True,"whatsapp":[]}]
for x in myresult:
  site = conectar(x['url']).iniciar()
  try:
    soup = BeautifulSoup(site.content, 'html.parser')
    img = soup.find_all('img',limit=False)
    imgBruto = conectar(x['url']+"/"+img[0]['src']).iniciar().content
    try:
        salvarOriginal(x['url'],x['_id'],img[0]['src'],x['banca'],imgBruto)
        salvar50por50(x['url'],x['_id'],img[0]['src'],x['banca'],imgBruto)
    except FileNotFoundError:
        os.mkdir(PATH)
        salvarOriginal(x['url'],x['_id'],img[0]['src'],x['banca'],imgBruto)
        salvar50por50(x['url'],x['_id'],img[0]['src'],x['banca'],imgBruto)
  except:
    print('ERRO NO LINK ABAIXO '+x['url'])
    traceback.print_exc()



PATH="/home/origin/www/oddsing/laravelOddsing/storage/app/bancas/"
URL_BASE="https://oddsing.xyz/bancas"
