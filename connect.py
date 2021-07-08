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
        return self.response.content
    def getResponseCode(self):
        return self.response.status_code
class ConectKbets():
    def __init__(self,link):
        self.link   = link
        self.response   = self.setResponse()
    def setResponse(self):
        r = requests.get(self.link)
        return r

    def getBody(self):
        return self.response.json()
        
    def getResponseCode(self):
        return self.response.status_code

