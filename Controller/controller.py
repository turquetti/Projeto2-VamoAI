from Model.model import NasaModel

class NasaController:
    retorna_obj = []

    def __init__(self):
        self.model = NasaModel()

    def search(self, ano, tipo):
        if tipo == 'csv':
            retorna_obj = self.model.retorna_csv(ano)
        elif tipo =='json':
            retorna_obj = self.model.retorna_json(ano)
        return retorna_obj
    
    def id(self):
        lista_id = []
        
        for i in range(0, retorna_obj['projects']['totalCount'] + 1):
            for j in retorna_obj['projects']['projects'][i-1].values():
                if type(j) == int:
                lista_id.append(j)

        return lista_id
    