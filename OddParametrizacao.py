class bolinhaParaSa():
    def __init__(self,codigo = '',nome = ''):
        self.grupoCodigo = int(codigo)
        self.grupoOdd = codigo
        self.tipoOdd  = ''
        self.nome = nome
    def getGrupoOdd(self):
        grupo = {
            1: "Vencedor do Encontro" ,
            2: "Dupla Chance" ,
            3: "Casa - Total de gols no jogo" ,
            4: "Fora - Total de gols no jogo" ,
            5: "Total de Gols no Jogo" ,
            6: "Ambas as equipes marcarão na partida" ,
            7: "Total de Gols Par ou Ímpar" ,
            8: "Resultado Exato" ,
            9: "Handicap de Gol" ,
            10: "Handicap Asiático" ,
            11: "Vence ao Intervalo/Vence ao Final do Jogo" ,
            12: "Empate não tem aposta" ,
            13: "Resultado / Total de Gols" ,
            14: "Ambas com Resultado" ,
            15: "Ambas as equipes marcarão na partida" ,
            16: "Margem de vitória" ,
            17: "Cantos" ,
            18: "Equipes para marcar" ,
            19: "Metados com mais gols" ,
            20: "Casa metade mais produtiva" ,
            21: "Fora metade mais produtiva" ,
            22: "Baliza inviolada" ,
            23: "Número de gols na partida" ,
            24: "Total de gols com ambas marcam" ,
            25: "Total exato de gols" ,
            26: "Ganhar a zero" ,
            27: "Ganhar um tempo" ,
            28: "Ganhar ambos os tempos" ,
            29: "Marcar em ambos os tempos" ,
            30: "1º Tempo - ambas as equipes marcam" ,
            31: "2º Tempo - ambas as equipes para marcar" ,
            32: "Marcar um pênalti" ,
            33: "Cartão vermelho na partida" ,
            40: "Vencedor da luta" ,
            45: "Vencedor" ,
            46: "Handicap de pontos" ,
            47: "Total de pontos" ,
            48: "Intervalo / Final" ,
            49: "Margem de vitória" ,
            50: "Casa Par/Ímpar" 
        }
        key = grupo.get(self.grupoCodigo)
        return key if key != None else 'desconecido: codigo '+str(self.grupoCodigo)
    def getName(self):
        grupo = {
        1: {
                 "Vencedor do Encontro": {
                    1:'Casa',
                    2:'Empate',
                    3:'Fora'
                }
             },
        2: {
                 "Dupla Chance":{
                    "1-2":"Casa ou Fora",
                    "1X":"Casa ou Empate",
                    "X2":"Empate ou Fora",
                }
            } ,
        3: {
                 "Casa - Total de gols no jogo": {
                    "Casa - Acima 0.5":"mais de 0,5",
                    "Casa - Acima 1.5":"mais de 1,5",
                    "Casa - Acima 2.5":"mais de 2,5",
                    "Casa - Acima 3.5":"mais de 3,5",
                    "Casa - Acima 4.5":"mais de 4,5",
                    "Casa - menos 0.5":"menos de 0,5",
                    "Casa - menos 1.5":"menos de 1,5",
                    "Casa - menos 2.5":"menos de 2,5",
                    "Casa - menos 3.5":"menos de 3,5",
                    "Casa - menos 4.5":"menos de 4,5",
                }
            } ,
        4: {
                 "Fora - Total de gols no jogo":{
                    "Fora - Acima 0.5":"mais de 0,5",
                    "Fora - Acima 1.5":"mais de 1,5",
                    "Fora - Acima 2.5":"mais de 2,5",
                    "Fora - Acima 3.5":"mais de 3,5",
                    "Fora - Acima 4.5":"mais de 4,5",
                    "Fora - menos 0.5":"menos de 0,5",
                    "Fora - menos 1.5":"menos de 1,5",
                    "Fora - menos 2.5":"menos de 2,5",
                    "Fora - menos 3.5":"menos de 3,5",
                    "Fora - menos 4.5":"menos de 4,5",
                 }
                } ,
        5: {
            "Total de Gols no Jogo":{
                 
                "Jogo - Acima 0.5":"mais de 0,5",
                "Jogo - Acima 1.5":"mais de 1,5",
                "Jogo - Acima 2.5":"mais de 2,5",
                "Jogo - Acima 3.5":"mais de 3,5",
                "Jogo - Acima 4.5":"mais de 4,5",
                "Jogo - menos 0.5":"menos de 0,5",
                "Jogo - menos 1.5":"menos de 1,5",
                "Jogo - menos 2.5":"menos de 2,5",
                "Jogo - menos 3.5":"menos de 3,5",
                "Jogo - menos 4.5":"menos de 4,5",
             }
            } ,
        6: {
                "Ambas as equipes marcarão na partida": {
                    "Ambos M Nao":"não",
                    "Ambos M":"sim"
                }
            } ,
        7: {"Total de Gols Par ou Ímpar": {
                "Casa": "Casa",
                "Fora": "Fora",
                "Empate":"Empate"
        }} ,
        8: {"Resultado Exato": {
        }} ,
        9: {"Handicap de Gol": {}} ,
        10:{ "Handicap Asiático": {}} ,
        11: {"Vence ao Intervalo/Vence ao Final do Jogo": {}} ,
        12: {"Empate não tem aposta": {}} ,
        13: {"Resultado / Total de Gols": {}} ,
        14: {"Ambas com Resultado": {}} ,
        15: {"Ambas as equipes marcarão na partida": {}} ,
        16: {"Margem de vitória": {}} ,
        17: {"Cantos": {}} ,
        18: {"Equipes para marcar": {}} ,
        19: {"Metados com mais gols": {}} ,
        20: {"Casa metade mais produtiva": {}} ,
        21: {"Fora metade mais produtiva": {}} ,
        22: {"Baliza inviolada": {}} ,
        23: {"Número de gols na partida": {}} ,
        24: {"Total de gols com ambas marcam": {}} ,
        25: {"Total exato de gols": {}} ,
        26: {"Ganhar a zero": {}} ,
        27: {"Ganhar um tempo" : {}},
        28: {"Ganhar ambos os tempos": {}} ,
        29: {"Marcar em ambos os tempos" : {}},
        30: {"1º Tempo - ambas as equipes marcam": {}} ,
        31: {"2º Tempo - ambas as equipes para marcar": {}} ,
        32: {"Marcar um pênalti": {}} ,
        33: {"Cartão vermelho na partida": {}} ,
        40: {"Vencedor da luta": {}} ,
        45: {"Vencedor": {}} ,
        46: {"Handicap de pontos": {}},
        47: {"Total de pontos" : {}},
        48: {"Intervalo / Final": {}} ,
        49: {"Margem de vitória" : {}},
        50: {"Casa Par/Ímpar": {}} 
        }
        grupamento = self.getGrupoOdd()
        key = grupo[self.grupoCodigo][grupamento].get(self.nome)
        return key if key != None else self.nome
class kbetsParaSa():
    def __init__(self,codigo = '',nome = '', tipoOdd = ''):
        self.grupoCodigo = int(codigo)
        self.grupoOdd = codigo
        self.tipoOdd  = tipoOdd
        self.nome = nome
    def getGrupoOdd(self):
        grupo = {
            1: "Vencedor do Encontro" ,
            2: "Dupla Chance" ,
            3: "Casa - Total de gols no jogo" ,
            4: "Fora - Total de gols no jogo" ,
            5: "Total de Gols no Jogo" ,
            6: "Ambas as equipes marcarão na partida" ,
            7: "Total de Gols Par ou Ímpar" ,
            8: "Resultado Exato" ,
            #9: "Handicap de Gol" ,
            #10: "Handicap Asiático" ,
            #11: "Vence ao Intervalo/Vence ao Final do Jogo" ,
            #12: "Empate não tem aposta" ,
            #13: "Resultado / Total de Gols" ,
            #14: "Ambas com Resultado" ,
            #15: "Ambas as equipes marcarão na partida" ,
            13: "Margem de vitória" ,
            48: "Cantos" ,
            #18: "Equipes para marcar" ,
            15: "Metados com mais gols" ,
            #20: "Casa metade mais produtiva" ,
            #21: "Fora metade mais produtiva" ,
            #22: "Baliza inviolada" ,
            16: "Número de gols na partida" ,
            17: "Total de gols com ambas marcam" ,
            18: "Total exato de gols" ,
            19: "Ganhar a zero" ,
            20: "Ganhar um tempo" ,
            21: "Ganhar ambos os tempos" ,
            22: "Marcar em ambos os tempos" ,

            30: "1º Tempo - ambas as equipes marcam" ,
            36: "2º Tempo - ambas as equipes para marcar" ,
            #32: "Marcar um pênalti" ,
            33: "Cartão vermelho na partida" ,
            #40: "Vencedor da luta" ,
            #45: "Vencedor" ,
            #46: "Handicap de pontos" ,
            #47: "Total de pontos" ,
            #48: "Intervalo / Final" ,
            #49: "Margem de vitória" ,
            #50: "Casa Par/Ímpar" 
        }
        key = grupo.get(self.grupoCodigo)
        return key if key != None else self.tipoOdd
    def getName(self):
        grupo = {
            1: { "Vencedor do Encontro" : {
                    "Casa": "Casa",
                    "Fora": "Fora",
                    "Empate": "Empate"
                }
            } ,
            2: { "Dupla Chance" :  {
                    "1-2 - Casa ou Fora":"Casa ou Fora",
                    "1X - Casa ou empate":"Casa ou Empate",
                    "X2 - Fora ou empate":"Empate ou Fora",
                }
            } ,
            3: { "Casa - Total de gols no jogo" : 
                {
                    "Casa Acima 0.5":"mais de 0,5",
                    "Casa Acima 1.5":"mais de 1,5",
                    "Casa Acima 2.5":"mais de 2,5",
                    "Casa Acima 3.5":"mais de 3,5",
                    "Casa Acima 4.5":"mais de 4,5",
                    "Casa Acima 5.5":"mais de 5,5",
                    "Casa Abaixo  0.5":"menos de 0,5",
                    "Casa Abaixo  1.5":"menos de 1,5",
                    "Casa Abaixo  2.5":"menos de 2,5",
                    "Casa Abaixo  3.5":"menos de 3,5",
                    "Casa Abaixo  4.5":"menos de 4,5",
                    "Casa Abaixo  5.5":"menos de 5,5",
                 }
            } ,
            4: { "Fora - Total de gols no jogo" : {
                    "Fora Acima 0.5":"mais de 0,5",
                    "Fora Acima 1.5":"mais de 1,5",
                    "Fora Acima 2.5":"mais de 2,5",
                    "Fora Acima 3.5":"mais de 3,5",
                    "Fora Acima 4.5":"mais de 4,5",
                    "Fora Acima 5.5":"mais de 5,5",
                    "Fora Abaixo 0.5":"menos de 0,5",
                    "Fora Abaixo 1.5":"menos de 1,5",
                    "Fora Abaixo 2.5":"menos de 2,5",
                    "Fora Abaixo 3.5":"menos de 3,5",
                    "Fora Abaixo 4.5":"menos de 4,5",
                    "Fora Abaixo 5.5":"menos de 5,5",
                 }
            } ,
            5: { "Total de Gols no Jogo" : {
                "Jogo - acima 0.5":"mais de 0,5",
                "Jogo - acima 1.5":"mais de 1,5",
                "Jogo - acima 2.5":"mais de 2,5",
                "Jogo - acima 3.5":"mais de 3,5",
                "Jogo - acima 4.5":"mais de 4,5",
                "Jogo - acima 5.5":"mais de 5,5",
                "Jogo - abaixo 0.5":"menos de 0,5",
                "Jogo - abaixo 1.5":"menos de 1,5",
                "Jogo - abaixo 2.5":"menos de 2,5",
                "Jogo - abaixo 3.5":"menos de 3,5",
                "Jogo - abaixo 4.5":"menos de 4,5",
                "Jogo - abaixo 5.5":"menos de 5,5",
                }  
            },
            6: { "Ambas as equipes marcarão na partida" : {} } ,
            7: { "Total de Gols Par ou Ímpar" : {} } ,
            8: { "Resultado Exato"  : {
                "Placar 0x0 Final":"0:0",
                "Placar 0x1 Final":"0:1",
                "Placar 0x2 Final":"0:2",
                "Placar 0x3 Final":"0:3",
                "Placar 0x4 Final":"0:4",
                "Placar 0x5 Final":"0:5",
                "Placar 0x6 Final":"0:6",

                "Placar 1x0 Final":"1:0",
                "Placar 1x1 Final":"1:1",
                "Placar 1x2 Final":"1:2",
                "Placar 1x3 Final":"1:3",
                "Placar 1x4 Final":"1:4",
                "Placar 1x5 Final":"1:5",
                "Placar 1x6 Final":"1:6",

                "Placar 2x0 Final":"2:0",
                "Placar 2x1 Final":"2:1",
                "Placar 2x2 Final":"2:2",
                "Placar 2x3 Final":"2:3",
                "Placar 2x4 Final":"2:4",
                "Placar 2x5 Final":"2:5",
                "Placar 2x6 Final":"2:6",
                
                "Placar 3x0 Final":"3:0",
                "Placar 3x1 Final":"3:1",
                "Placar 3x2 Final":"3:2",
                "Placar 3x3 Final":"3:3",
                "Placar 3x4 Final":"3:4",
                "Placar 3x5 Final":"3:5",
                "Placar 3x6 Final":"3:6",

                "Placar 4x0 Final":"4:0",
                "Placar 4x1 Final":"4:1",
                "Placar 4x2 Final":"4:2",
                "Placar 4x3 Final":"4:3",
                "Placar 4x4 Final":"4:4",
                "Placar 4x5 Final":"4:5",
                "Placar 4x6 Final":"4:6",

                "Placar 5x0 Final":"5:0",
                "Placar 5x1 Final":"5:1",
                "Placar 5x2 Final":"5:2",
                "Placar 5x3 Final":"5:3",
                "Placar 5x4 Final":"5:4",
                "Placar 5x5 Final":"5:5",
                "Placar 5x6 Final":"5:6",

                "Placar 6x0 Final":"6:0",
                "Placar 6x1 Final":"6:1",
                "Placar 6x2 Final":"6:2",
                "Placar 6x3 Final":"6:3",
                "Placar 6x4 Final":"6:4",
                "Placar 6x5 Final":"6:5",
                "Placar 6x6 Final":"6:6",


            } },
            #9: "Handicap de Gol" ,
            #10: "Handicap Asiático" ,
            #11: "Vence ao Intervalo/Vence ao Final do Jogo" ,
            #12: "Empate não tem aposta" ,
            #13: "Resultado / Total de Gols" ,
            #14: "Ambas com Resultado" ,
            #15: "Ambas as equipes marcarão na partida" ,
            13: { "Margem de vitória" : {} } ,
            48: { "Cantos" : {} } ,
            #18: "Equipes para marcar" ,
            15: { "Metados com mais gols" : {} } ,
            #20: "Casa metade mais produtiva" ,
            #21: "Fora metade mais produtiva" ,
            #22: "Baliza inviolada" ,
            16: { "Número de gols na partida" : {} } ,
            17: { "Total de gols com ambas marcam" : {} } ,
            18: { "Total exato de gols" : {} } ,
            19: { "Ganhar a zero" : {} } ,
            20: { "Ganhar um tempo" : {} } ,
            21: { "Ganhar ambos os tempos" : {} } ,
            22: { "Marcar em ambos os tempos" : {} } ,
            30: { "1º Tempo - ambas as equipes marcam" : {} } ,
            36: { "2º Tempo - ambas as equipes para marcar" : {} } ,
            #32: "Marcar um pênalti" ,
            33: { "Cartão vermelho na partida" : {} } ,
            #40: "Vencedor da luta" ,
            #45: "Vencedor" ,
            #46: "Handicap de pontos" ,
            #47: "Total de pontos" ,
            #48: "Intervalo / Final" ,
            #49: "Margem de vitória" ,
            #50: "Casa Par/Ímpar" 
        }

        grupamento = self.getGrupoOdd()
        try:
            key = grupo[self.grupoCodigo][grupamento].get(self.nome,self.nome)
        except:
            key = self.nome
        return key 

#a = kbetsParaSa(17,'Jogo - Acima 1.5','empate ou fora')
#print(a.getGrupoOdd())
#print(a.getName())
