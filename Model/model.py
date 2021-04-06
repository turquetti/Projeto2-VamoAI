import requests
import json 
import pandas as pd

class NasaModel:

    # path = '/Users/gabrielaturquetti/Documents/Projeto-2-vamoai/Projeto2-VamoAI/api_key.txt'
    # arquivo = open(path,'r')
    lista_json = []
    
    def __init__(self):
        self.url = "https://api.nasa.gov/planetary/apod"
        # self.api_key = self.arquivo.read()
        self.api_key = 'F8pxcg3lpaCoKgUISPrEQZwVKGY5G2IOdukbywfu'

    def retorna_json(self, quantidade):
        resposta = self.requisicao(quantidade)
        return resposta.json()

    def retorna_csv(self, quantidade):
        self.resposta = self.requisicao(quantidade)
        return self.json_to_csv(resposta.content)

    def requisicao(self, quantidade):
        return requests.get(f'{self.url}?api_key={self.api_key}&count={quantidade}')

    def json_to_csv(self, json):
        file = pd.read_json(json)
        return file.to_csv()

    def infos(self, quantidade):
        for i in range(0, quantidade):
            self.lista_json.append(self.retorna_json(quantidade))
        
        df = pd.DataFrame(self.lista_json[0])
        dados = df[['url','title','date','explanation']]
        return dados.to_json()
