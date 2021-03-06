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
    
    def input_baixar(self, opcao_tipo):
        self.opcao_tipo = opcao_tipo
    
    def baixar_arquivo(self):
        return self.controller.baixar(self.quantidade, self.opcao_tipo)

    def resposta(self):
        return self.controller.search(self.ano, self.tipo)

    def imprime_infos(self):
        return self.controller.validacao(self.quantidade)
    
