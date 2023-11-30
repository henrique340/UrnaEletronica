from arquivo import *

while True:
    Menu()
    opc = int(input('Digite sua escolha: '))
    if opc == 1:
        Cadastro_Candidatos()
    elif opc == 2:
        Cadastrar_Eleitores()
    elif opc == 3:
        Votar()
    elif opc == 4:
        Resultado()
    elif opc == 5:
        Relatorio()
    elif opc == 6:
        print('Encerrando o programa')
        sleep(1)
        break
    else:
        print('Erro, tente novamente')