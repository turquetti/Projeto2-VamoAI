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
        return self.infos(quantidade).to_json(r'/Users/gabrielaturquetti/Documents/Projeto-2-vamoai/Projeto2-VamoAI/Arquivos/vamoainasestrelas.json')

    def retorna_csv(self, quantidade):
        return self.infos(quantidade).to_csv(r'/Users/gabrielaturquetti/Documents/Projeto-2-vamoai/Projeto2-VamoAI/Arquivos/vamoainasestrelas.csv')

    def requisicao(self, quantidade):
        return requests.get(f'{self.url}?api_key={self.api_key}&count={quantidade}')

    def infos(self, quantidade):
        for i in range(0, quantidade):
            self.lista_json.append(self.requisicao(quantidade).json())
        
        df = pd.DataFrame(self.lista_json[0])

        dados = df[['url','title','date','explanation']]
        return dados

    def validacao_code(self , quantidade):
        self.retorno = self.requisicao(quantidade).status_code
        if self.retorno == 200:
            return self.infos(quantidade)
        elif self.retorno == 404:
            return ("Error 404 -  NOT FOUND\n"
                    "O Endereço a seguir não foi encontrado!\n"
                    "Verifique se o endereço está correto e tente novamente.")
        elif self.retorno == 500:
            return ("Error 500 -  INTERNAL SERVER ERROR\n"
                    "Erro interno do servidor. Tente novamente dentro de minutos.")
        elif self.retorno == 401:
            return ("Error 401 - UNAUTHORIZED\n"
                    "Verifique se suas crendeciais estão corretas e tente novamente.")
        elif self.retorno == 400:
            return ("Error 400 -  BAD REQUEST\n"
                    "Não foi possível processar sua requisição. Verifique as informações e tente novamente.")
        elif self.retorno == 403:
            return ("Error 403 - FORBIDDEN\n"
                    "Você não tem permissão de acesso nesse servidor.")
        else:
            return (f"Erro não identificado.\n"
                    f"Entre em contato com o Vamo AI nas estrelas e informe o {self.retorno}."
                    f"Ou verifique o erro no site https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status")