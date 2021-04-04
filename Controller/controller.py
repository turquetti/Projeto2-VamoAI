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
    
    def infos(self, quantidade):
        for i,j in self.model.retorna_json(quantidade)[0].items():
            if i == 'url':
                self.dic_infos['Url'] = j
            if i == 'title':
                self.dic_infos['Title'] = j
            if i == 'date':
                self.dic_infos['Date'] = j
            if i == 'explanation':
                self.dic_infos['Explanation'] = j
            self.lista_projetos.append(self.dic_infos)
        print(self.lista_projetos)
        return self.lista_projetos


