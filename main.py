from View.view import NasaView

view = NasaView()

print(" ✩ "* 60)
print('''
                                                             __        /          __   __ _____ __  __        __        
                                                \  / /\ |\/|/  \   /\ |  |\ | /\ (_   |_ (_  | |__)|_ |   /\ (_         
                                                 \/ /--\|  |\__/  /--\|  | \|/--\__)  |____) | | \ |__|__/--\__)        

''')
print(" ✩ "* 60)

print('''
Olá tripulante,
Você está pronto para embarcar nessa aventura? 
''')

view.input_quantidade(int(input(("Digite o número de eventos astronômicos que você gostaria de ver: "))))

print(' '*100)

print('''
Você deseja visualizar os eventos astronômicos ou baixar as informações?

[ 1 ] Visualizar
[ 2 ] Baixar

''')

input_visualizacao = int(input("Digite sua opção: "))

if input_visualizacao == 1:
    return view.imprime_infos()

elif input_visualizacao == 2: 
    print('''
    Você deseja baixar os eventos em:
    [ 1 ] JSON
    [ 2 ] CSV
    ''')

    view.input_baixar(int(input("Digite sua opção: ")))

    return view.metodoqueagentenaocriouAINDAkkkkk
else: 
    print("Entrada Inválida")

print(' '*100)

print(' ' * 100)

