import requests

#essa class faz a primeira requisição ao site
class ConectSA():
    def __init__(self,SALink):
        self.link   = SALink
        self.response   = self.setResponse()
    def setResponse(self):
        r = requests.get(self.link)
        return r

    def getBody(self):
        return self.response.text
    def getResponseCode(self):
        return self.response.status_code

