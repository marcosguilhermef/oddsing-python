import datasets
import scrapingLinks
from datasets import Link
from lerArquivoDeLinks import ArquivoSA as lerSa
from connect import ConectSA
class CarregamentoDeLinks():
    def __init__(self):
        self.links = self.carregamentoSa()
    def carregamentoSa(self):
        links = lerSa().ler()
        datasets = Link(links)
        return Link.getLinkList()
    def ScrapingLinks(self):
        for link in self.links:
            responseCode = ConectSA(link).getResponseCode()
            print(link,'  :  ',responseCode)




a = CarregamentoDeLinks()
print(a.ScrapingLinks())