class Oddssa():
    def __init__(self,list):
        self.casa = list['casa']
        self.fora = list['fora']
        self.empate = list['empate']
class Link():
    lengthList = 0
    interator  = 0
    link       = None
    def __init__(self,list):        
        self.setLinkList(list)
        self.setLengthList()
        self.setInterator()

    #link list
    @staticmethod
    def getLinkList():
        print('setado')
        return Link.link
    def setLinkList(self,list):
        Link.link = list
    
    #interator
    @staticmethod
    def getInterator():
        return Link.interator

    @staticmethod
    def incrementInterator():
        return Link.interator+1

    def setInterator(self):
        Link.interator = 0

    #lengthlist
    @staticmethod
    def getLengthList():
        return Link.lengthList

    def setLengthList(self):
        Link.lengthList = len(self.link)

    


    

