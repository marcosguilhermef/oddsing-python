class Oddssa():
    def __init__(self,list,body):
        self.banca = list['banca']
        self.campeonato = list['campeonato']

        self.tCasa = list['tCasa']
        self.tFora = list['tFora']

        self.casa = list['casa']
        self.empate = list['empate']
        self.fora = list['fora']
        self.body = body
    
    def setTCasa(self, value):
        self.tCasa = value
    def setTFora(self, value):
        self.tFora = value
    def setFora(self, value):
        self.fora = value
    def setEmpate(self, value):
        self.empate = value
    def setCasa(self, value):
        self.casa = value
    def setCampeonato(self, value):
        self.campeonato = value


class Link():

    """def __init__(self,list):        
        self.setLinkList(list)
        self.setLengthList()
        self.setInterator()"""
    def __init__(self,list):   
        self.setLinkList(list)
        self.setLengthList()
        self.setInterator()

    #link list
    def getLinkList(self):
        print('setado',self.link)
        return self.link
    def setLinkList(self,list):
        self.link = list
    
    #interator
    def getInterator(self):
        return self.interator

    def incrementInterator(self):
        self.interator =+ 1
        return self.interator

    def setInterator(self):
        self.getInterator = 0

    #lengthlist
    def getLengthList(self):
        return self.lengthList

    def setLengthList(self):
        self.lengthList = len(self.link)

    


    

