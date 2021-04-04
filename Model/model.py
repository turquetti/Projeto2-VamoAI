import requests
import json 
import pandas as pd
class NasaModel:

    path = 'C:/Users/soare/Documents/Projetos/Projeto2-VamoAI/api_key.txt'
    arquivo = open(path,'r')
    
    def __init__(self):
        self.url = "https://api.nasa.gov/planetary/apod"
        self.api_key = self.arquivo.read()

    def retorna_json(self, quantidade):
        resposta = self.requisicao(quantidade)
        return resposta.json()

    def retorna_csv(self, quantidade):
        resposta = self.requisicao(quantidade)
        return self.json_to_csv(resposta.content)

    def requisicao(self, quantidade):
        return requests.get(f'{self.url}?api_key={self.api_key}&count={quantidade}')


    def json_to_csv(self, json):
        file = pd.read_json(json)
        return file.to_csv()



