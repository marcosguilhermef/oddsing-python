import requests

#essa class faz a primeira requisição ao site
class ConectSA():
    def __init__(self,SALink):
        self.link   = SALink
        self.response   = self.setResponse()
    def setResponse(self):
        try:
            r = requests.get('https://'+self.link)
            return r
        except requests.exceptions.SSLError:
            r = requests.get('http://'+self.link)
            return r
        except Exception as erro:
            raise erro

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
            return r
        except requests.exceptions.SSLError:
            print('http://'+self.link)
            r = requests.get('http://'+self.link)
            return r
        except Exception as erro:
            raise erro

    def getBody(self):
        return self.response.json()
        
    def getResponseCode(self):
        return self.response.status_code

class Cookie():
    cookies = None
    def setCookie(self,cookie):
        self.cookies = cookie
    
class ConectBolinha():
    cookies = ''
    def __init__(self,link):
        self.link   = link
        self.response   = self.setResponse()
    def setResponse(self):
        try:
            print('https://'+self.link)
            a = Cookie()
            r = requests.get('https://'+self.link, cookies = a.cookies)
            a.setCookie(r.cookies)

            if r.status_code == 500:
                raise  requests.exceptions.ConnectionError
            return r
        except requests.exceptions.SSLError:
            print('http://'+self.link)
            a = Cookie()
            r = requests.get('http://'+self.link, cookies = a.cookies)
            a.setCookie(r.cookies)
            if r.status_code == 500:
                raise  requests.exceptions.ConnectionError
            return r
        except requests.exceptions.ConnectionError:
            try:
                """ proxies = {
                    "http": "http://lum-customer-hl_6fcc0e29-zone-static-route_err-pass_dyn-country-br:1art1pt9d8mi@zproxy.lum-superproxy.io:22225",
                    "https": "http://lum-customer-hl_6fcc0e29-zone-static-route_err-pass_dyn-country-br:1art1pt9d8mi@zproxy.lum-superproxy.io:22225",
                } """
                proxies = {
                    "http": "socks4://191.7.215.246:5678",
                    "https": "socks4://191.7.215.246:5678",
                }
                print('http://'+self.link)
                r = requests.get('https://'+self.link, proxies=proxies)
                return r
            except:
                print('http://'+self.link)
                print('erro')
                r = requests.get('http://'+self.link, proxies = proxies)
                return r

        

    def getBody(self):
        return self.response.json()
        
    def getResponseCode(self):
        return self.response.status_code

