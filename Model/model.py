import requests
import json 
import pandas as pd 



class NasaModel:
    
    path = '/Users/gabrielaturquetti/Documents/Projeto-2-vamoai/Projeto2-VamoAI/api_key.txt'
    arquivo = open(path,'r')
    
    def __init__(self):
        self.url = "https://api.nasa.gov/techport/api/projects"
        self.api_key = self.arquivo.read()

    def retorna_json(self, ano):
        resposta = self.requisicao(ano)
        return resposta.json()

    def retorna_csv(self, ano):
        resposta = self.requisicao(ano)
        return self.json_to_csv(resposta.content)

    def requisicao(self, ano):
        return requests.get(f'{self.url}?updatedSince={ano}-01-01&api_key={self.api_key}')
  
    def json_to_csv(self, json):
        file = pd.read_json(json)
        return file.to_csv()

    def requisicao_id(self, id):
        return requests.get(f'/{id}?api_key={self.api_key}')

