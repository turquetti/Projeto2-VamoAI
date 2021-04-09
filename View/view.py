from Controller.controller import NasaController  

class NasaView:
    def __init__(self):
        self.controller = NasaController()

    def input_ano(self, ano):
        self.ano = ano
    
    def input_tipo(self, tipo):
        self.tipo = tipo

    def input_quantidade(self,quantidade):
        self.quantidade = quantidade

    def resposta(self):
        return self.controller.search(self.ano, self.tipo)

    def imprime_infos(self):
        return self.controller.infos(self.quantidade)
    
