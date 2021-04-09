from Model.model import NasaModel

class NasaController:
    retorna_obj = []
    dic_infos = {}
    lista_projetos = []

    def __init__(self):
        self.model = NasaModel()

    def baixar(self, quantidade, opcao_tipo):
        if opcao_tipo == 1:
            return self.model.retorna_json(quantidade)
        elif opcao_tipo == 2:
            return self.model.retorna_csv(quantidade)

    def validacao(self, quantidade):
        return self.model.validacao_code(quantidade)


