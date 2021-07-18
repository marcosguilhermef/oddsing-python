import requests

#essa class faz a primeira requisição ao site
class ConectSA():
    def __init__(self,SALink):
        self.link   = SALink
        self.response   = self.setResponse()
    def setResponse(self):
        try:
            r = requests.get('https://'+self.link)
        except requests.exceptions.SSLError:
            r = requests.get('http://'+self.link)
        except:
            pass
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
        try:
            print('https://'+self.link)
            r = requests.get('https://'+self.link)
        except requests.exceptions.SSLError:
            print('http://'+self.link)
            r = requests.get('http://'+self.link)
        except:
            pass
        return r

    def getBody(self):
        return self.response.json()
        
    def getResponseCode(self):
        return self.response.status_code

