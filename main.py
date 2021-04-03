from View.view import NasaView

print("="*100)
print("NASA TECHPORT")
print("="*100)

info_techport = NasaView()

info_techport.input_ano(input("Digite o ano que você gostaria de pesquisar os projetos da NASA: "))
info_techport.input_tipo(input("Digite 'json' ou 'csv' para exportar seu arquivo: "))
print(info_techport.resposta())