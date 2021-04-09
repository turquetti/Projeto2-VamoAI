from View.view import NasaView
from Controller.controller import NasaController
from Model.model import NasaModel

print("="*100)
print(
'''NASA TECHPORT'''
)
print("="*100)

info_techport = NasaView()

info_mode = NasaController()

model = NasaModel()

#info_techport.input_ano(input("Digite o ano que você gostaria de pesquisar os projetos da NASA: "))
# info_techport.input_tipo(input("Digite 'json' ou 'csv' para exportar seu arquivo: "))
#info_techport.input_quantidade(int(input("Digite a quantidade de imagens que você gostaria de ver: ")))

#print(info_techport.imprime_infos())

#print(model.infos(1))
print(model.requisicao(1))
