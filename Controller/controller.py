from Model.model import NasaModel

class NasaController:
    def __init__(self):
        self.model = NasaModel()

    def search(self, ano, tipo):
        retorna_obj = []

        if tipo == 'csv':
            retorna_obj = self.model.retorna_csv(ano)
        elif tipo =='json':
            retorna_obj = self.model.retorna_json(ano)

        return retorna_obj
    