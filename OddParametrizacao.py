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
        7: {"Total de Gols Par ou Ímpar": {}} ,
        8: {"Resultado Exato": {}} ,
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

#a = bolinhaParaSa(5,'Jogo - Acima 1.5')
#print(a.getGrupoOdd())
#print(a.getName())
