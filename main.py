from View.view import NasaView

class Main():
    view = NasaView()
    
    def repetir():
        input_pergunta = input("Deseja consultar outro evento? [S/N] ").strip().upper()
        if input_pergunta == 'N':
            return False
        else:
            return True

    while True:
        print(" ✩ "* 55)
        print('''
                                                                     __        /          __   __ _____ __  __        __        
                                                 |      \  / /\ |\/|/  \   /\ |  |\ | /\ (_   |_ (_  | |__)|_ |   /\ (_        
                                               /   \     \/ /--\|  |\__/  /--\|  | \|/--\__)  |____) | | \ |__|__/--\__)            
                                              /  __ \   
                                              |.' '.|
                                            ,'|'._.'|`. 
                                           |,'|__|__|-.|
        ''')

        print(" ✩ "* 55)

        print('''
Olá tripulante,

Você está pronto para embarcar nessa aventura? 🚀
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
            print(view.imprime_infos())

        elif input_visualizacao == 2: 
            print('''
Você deseja baixar os eventos em:
[ 1 ] JSON
[ 2 ] CSV
            ''')

            view.input_baixar(int(input("Digite sua opção: ")))

            view.baixar_arquivo()
            print(' '*100)            
            print("Download realizado com sucesso!")
            print(' '*100)
        else: 
            print("Entrada Inválida")

        print(' '*100)

        print(' ' * 100)

        if not repetir():
            break
        else:
            continue
                      