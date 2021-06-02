import re

class ArquivoSA():
    def ler(self):
        op = open('SAlist')
        links = op.readlines()
        return list(map(lambda link : re.sub('\n','',link), links))

class ArquivoKBETS():
    def ler(self):
        op = open('KBETSlist')
        links = op.readlines()
        return list(map(lambda link : re.sub('\n','',link), links))
