from Model.model import NasaModel

class NasaController:
    retorna_obj = []
    dic_infos = {}
    lista_projetos = []

    def __init__(self):
        self.model = NasaModel()

    def search(self, quantidade, tipo):
        if tipo == 'csv':
            retorna_obj = self.model.retorna_csv(quantidade)
        elif tipo =='json':
            retorna_obj = self.model.retorna_json(quantidade)

        return retorna_obj
    



