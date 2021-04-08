import requests
import json 
import pandas as pd
from pandas import util

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 500)
# pd.set_option('display.width', pd.util.terminal.get_terminal_size()[0])

class NasaModel:

    # path = '/Users/gabrielaturquetti/Documents/Projeto-2-vamoai/Projeto2-VamoAI/api_key.txt'
    # arquivo = open(path,'r')
    lista_json = []
    
    def __init__(self):
        self.url = "https://api.nasa.gov/planetary/apod"
        # self.api_key = self.arquivo.read()
        self.api_key = 'F8pxcg3lpaCoKgUISPrEQZwVKGY5G2IOdukbywfu'

    def retorna_json(self, quantidade):
        return self.infos(quantidade).to_json('vamoainasestrelas.json')

    def retorna_csv(self, quantidade):
        return self.infos(quantidade).to_csv('vamoainasestrelas.csv')

    def requisicao(self, quantidade):
        return requests.get(f'{self.url}?api_key={self.api_key}&count={quantidade}')

    def infos(self, quantidade):
        for i in range(0, quantidade):
            # self.lista_json.append(self.retorna_json(quantidade))
            self.lista_json.append(self.requisicao(quantidade).json())
        
        df = pd.DataFrame(self.lista_json[0])
        #pd.set_option("display.max_colwidth", None)

        dados = df[['url','title','date','explanation']]
        return dados

    def validacao_code(self , quantidade):  # Validacao do Codigo feito em diversos retornos e erros
        self.retorno = self.requisicao(quantidade).status_code
        if self.retorno == 200:
            return self.infos(quantidade)
        elif self.retorno == 404:
            return ("Erro 404. Not Found\n"
                    "O Endereço a seguir não foi encontrado\n"
                    "Verifique se o endereço, esta correto e tente novamente")
        elif self.retorno == 500:
            return ("Erro 500. Internal Server Error/n"
                    "Erro interno do servidor, Aguarde algum tempo para tentar novamente")
        elif self.retorno == 401:
            return ("Erro 401. Não Autorizado/n"
                    "Verifique se as sua Crendeciais,Senha ou login, estão corretas e tente novamente")
        elif self.retorno == 400:
            return ("Erro 400. Bad Request/n"
                    "Encontramos erros, Causas comuns - Texto mal formado - Caracteres Especiais -\n "
                    "ou requisição mal formada ")
        elif self.retorno == 403:
            return ("Erro 403. Forbidden\n"
                    "O Servidor entendeu o pedido, mais devido algum erro de credencial e impossivel\n"
                    "a autorização para visualização do conteudo")
        else:
            return ("Desculpe o codigo de erro não foi encontrado no momento\n"
                    "mais não se preocupe pois você pode verificar o codigo do erro \n"
                    "no site https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status")