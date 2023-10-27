
#Bibliotecas usadas na aplicação
from time import sleep
from operator import itemgetter
from collections import Counter

# Listas usadas na aplicação
count_pref = 0
count_gov = 0
count_pres = 0
CPF = []
lista_Candidatos_Governador = []
Partidos_Governador = []
lista_Voto_Governador = []
Voto_Branco_Governador = [0]
Voto_Nulo_Governador = [0]
Votos_Validos_Governador = [0]

lista_Candidatos_Presidente = []
Partidos_Presidente = []
lista_Voto_Presidente = []
Voto_Branco_Presidente = [0]
Voto_Nulo_Presidente = [0]
Votos_Validos_Presidente = [0]

lista_Candidatos_Prefeito = []
Partidos_Prefeito = []
lista_Voto_Prefeito = []
Voto_Branco_Prefeito = [0]
Voto_Nulo_Prefeito = [0]
Votos_Validos_Prefeito = [0]

eleitores_novo = []
lista_eleitores = []


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro')


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cabecalho(txt, tam):
    print('-' * tam)
    print(txt.center(tam))
    print('-' * tam)

def ler_arquivo(nome):
    global dado
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arq')
    else:
        cabecalho('compras', 42)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastro(arq, item, preco):
    try:
        a = open(arq, 'at')
    except:
        print('não foi possível abrir')
    else:
        try:
            a.write(f'{item}; R${preco:.2f}\n')
        except:
            print('erro ao inserir dado')
        else:
            print(f'{item} adicionado com sucesso')


# Função CLI do Menu-inicial
def Menu():
    print('-'*66)
    print('{:^66}'.format('+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++')) # Imprime o texto "MENU" centralizado em uma linha com 66 caracteres
    print('-' * 66)
    print('''1. Cadastrar Candidatos
2. Cadastrar Eleitores 
3. Votar
4. Apurar resultados
5. Relatórios e Estatísticas 
6. Encerrar ''')

# Função de cadastro para os canditados
def Cadastro_Candidatos():
    while True:
        print()
        print('-' * 66)
        print('{:^66}'.format('CADASTRO DE CANDIDATOS'))
        print('-' * 66)
        nome = input('Digite o nome do candidato: ').upper()
        while True:
            cargo = input('Digite o cargo do candidato: ').upper()
            if cargo == 'GOVERNADOR':
                lista_Candidatos_Governador.append(nome)
                numero = lista_Candidatos_Governador.index(nome)
                partido = input('Digite o partido do candidato: ').upper()
                Partidos_Governador.append(partido)
                print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                lista_Voto_Governador.append(nome)
                break
            elif cargo == 'PREFEITO':
                lista_Candidatos_Prefeito.append(nome)
                numero = lista_Candidatos_Prefeito.index(nome)
                partido = input('Digite o partido do candidato: ').upper()
                Partidos_Prefeito.append(partido)
                print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                lista_Voto_Prefeito.append(nome)
                break
            elif cargo == 'PRESIDENTE':
                lista_Candidatos_Presidente.append(nome)
                numero = lista_Candidatos_Presidente.index(nome)
                partido = input('Digite o partido do candidato: ').upper()
                Partidos_Presidente.append(partido)
                print(f'O candidato {nome} do numero {numero}, do partido {partido} e do cargo {cargo} foi adicionado com sucesso')
                lista_Voto_Presidente.append(nome)
                break
            else:
                print('Insira um cargo válido: ')
        opc = input('Deseja cadastrar outro candidato? [Sim]/[Nao] ').upper()
        if opc == 'NAO':
            break

# Função para cadastro de eleitores
def Cadastrar_Eleitores():
    global lista_eleitores, eleitores_novo
    while True:
        print()
        print('-' * 66)
        print('{:^66}'.format('CADASTRO DE ELEITORES'))
        print('-' * 66)
        nome = input('Digite o nome do eleitor: ').upper()
        if nome.isalpha():
            lista_eleitores.append(nome)
            eleitores_novo.append(nome)
            while True:
                cpf = input('Digite o CPF do eleitor: ')
                if len(cpf) == 11:
                    if cpf not in CPF:
                        CPF.append(cpf)
                        print(f'o eleitor {nome} de cpf {cpf} foi adicionado com sucesso')
                        print(lista_eleitores)
                        break
                    else:
                        print('Eleitor já foi cadastrado com esse cpf')
                else:
                    print('Digite um numero de cpf válido')
            opc = input('Deseja cadastrar outro candidato? [Sim]/[Nao] ').upper()
            if opc == 'NAO':
                break
        else:
            print('Erro, tente novamente')

# Função que realiza os votos (são coletados em 3 etapas: Prefeito -> Governador -> Presidente; ou seja, primeiramente o voto para Prefeito, em seguida para Governador e por fim para Presidente.)
def Votar():
    global count_gov, count_pref, count_pres, Voto_Branco_Prefeito, Voto_Nulo_Prefeito, Votos_Validos_Prefeito, Voto_Branco_Governador, Voto_Nulo_Governador, Votos_Validos_Governador, Voto_Branco_Presidente, Voto_Nulo_Presidente, Votos_Validos_Presidente, lista_Voto_Presidente, lista_Voto_Governador, lista_Voto_Prefeito, lista_eleitores, lista_Candidatos_Prefeito, lista_Candidatos_Presidente, lista_Candidatos_Governador
    print()
    print('-' * 66)
    print('{:^66}'.format('VOTAÇÃO'))
    print('-'*66)
    print(f'lista de eleitores: {eleitores_novo}')
    while True:
        nome = input('Digite o nome do eleitor: ').upper()
        if nome in lista_eleitores:
            eleitores_novo.remove(nome)
            # Repetição que cadastra os votos para <PREFEITO>
            while True:
                print('-' * 66)
                print('{:^66}'.format('Votação Prefeito'))
                print('-' * 66)
                print('Para votar branco [vote -1]')
                print('Para votar nulo [vote -2]')
                for i, candidato in enumerate(lista_Candidatos_Prefeito):
                    print(f'{i} - {candidato} ({Partidos_Prefeito[i]})')
                voto_prefeito = int(input('Digite seu voto: '))
                if voto_prefeito == -1:
                    print(f'O eleitor {nome} votou em branco')
                    confirmacao = input('Deseja confirmar o voto? [Sim]/[Não]] ').upper()
                    if confirmacao == 'SIM':
                        Voto_Branco_Prefeito[0] += 1
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('Erro, tente novamente')
                elif voto_prefeito == -2:
                    print(f'O eleitor {nome} votou nulo')
                    confirmacao = input('Deseja confirmar o voto? [Sim]/[Não] ').upper()
                    if confirmacao == 'SIM':
                        Voto_Nulo_Prefeito[0] += 1
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('Erro, tente novamente')
                elif voto_prefeito >= 0:
                    print(f'O número {voto_prefeito} é o candidato {lista_Candidatos_Prefeito[voto_prefeito]} do partido {Partidos_Prefeito[voto_prefeito]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não]] ').upper()
                    if confirmacao == 'SIM':
                        Votos_Validos_Prefeito[0] += 1

                        # Executa/Confirma o voto para o candidato selecionado
                        for i in range(len(lista_Candidatos_Prefeito)):
                            if lista_Candidatos_Prefeito[i] == lista_Voto_Prefeito[i]:
                                lista_Voto_Prefeito.remove(lista_Candidatos_Prefeito[i])
                                lista_Voto_Prefeito.insert(i, [lista_Candidatos_Prefeito[i], i, Partidos_Prefeito[i], 'PREFEITO', 0])
                            if lista_Candidatos_Prefeito[i] == lista_Voto_Prefeito[i][0]:
                                lista_Voto_Prefeito[i] = [lista_Candidatos_Prefeito[i], i, Partidos_Prefeito[i], 'PREFEITO', lista_Voto_Prefeito[i][4] + 1]
                            else:
                                lista_Voto_Prefeito[i] = [lista_Candidatos_Prefeito[i], i, Partidos_Prefeito[i],'PREFEITO', lista_Voto_Prefeito[i][4]]
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('opção inválida, tente novamente')

            # Repetição que cadastra os votos para <GOVERNADOR>
            while True:
                print('-' * 66)
                print('{:^66}'.format('Votação Governador'))
                print('-' * 66)
                print('Para votar branco [vote -1]')
                print('Para votar nulo [vote -2]')
                for i, candidato in enumerate(lista_Candidatos_Governador):
                    print(f'{i} - {candidato} ({Partidos_Governador[i]})')
                voto_governador = int(input('Digite seu voto: '))
                if voto_governador == -1:
                    print(f'O eleitor {nome} votou em branco')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não]] ').upper()
                    if confirmacao == 'SIM':
                        Voto_Branco_Governador[0] += 1
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('Erro, tente novamente')
                elif voto_governador == -2:
                    print(f'O eleitor {nome} votou nulo')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não] ').upper()
                    if confirmacao == 'SIM':
                        Voto_Nulo_Governador[0] += 1
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('Erro, tente novamente')
                elif voto_governador >= 0:
                    print(f'O número {voto_governador} é o candidato {lista_Candidatos_Governador[voto_governador]} do partido {Partidos_Governador[voto_governador]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não]] ').upper()
                    if confirmacao == 'SIM':
                        Votos_Validos_Governador[0] += 1

                        # Executa/Confirma o voto para o candidato selecionado
                        for i in range(len(lista_Candidatos_Governador)):
                            if lista_Candidatos_Governador[i] == lista_Voto_Governador[i]:
                                lista_Voto_Governador.remove(lista_Candidatos_Governador[i])
                                lista_Voto_Governador.insert(i, [lista_Candidatos_Governador[i], i, Partidos_Governador[i], 'GOVERNADOR', 0])
                            if lista_Candidatos_Governador[i] == lista_Voto_Governador[i][0]:
                                lista_Voto_Governador[i] = [lista_Candidatos_Governador[i], i, Partidos_Governador[i],'GOVERNADOR', lista_Voto_Governador[i][4] + 1]
                            else:
                                lista_Voto_Governador[i] = [lista_Candidatos_Governador[i], i, Partidos_Governador[i],'GOVERNADOR', lista_Voto_Governador[i][4]]
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('opção inválida, tente novamente')

            # Repetição que cadastra os votos para <PRESIDENTE>
            while True:
                print('-' * 66)
                print('{:^66}'.format('Votação Presidente'))
                print('-' * 66)
                print('Para votar branco [vote -1]')
                print('Para votar nulo [vote -2]')
                for i, candidato in enumerate(lista_Candidatos_Presidente):
                    print(f'{i} - {candidato} ({Partidos_Presidente[i]})')
                voto_presidente = int(input('Digite seu voto: '))
                if voto_presidente == -1:
                    print(f'O eleitor {nome} votou em branco')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não]] ').upper()
                    if confirmacao == 'SIM':
                        Voto_Branco_Presidente[0] += 1
                        print('Voto sendo adicionado ...')
                        sleep(2)
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('Erro, tente novamente')
                elif voto_presidente == -2:
                    print(f'O eleitor {nome} votou nulo')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não] ').upper()
                    if confirmacao == 'SIM':
                        Voto_Nulo_Presidente[0] += 1
                        print('Voto sendo adicionado ...')
                        sleep(2)
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('Erro, tente novamente')
                elif voto_presidente >= 0:
                    print(f'O número {voto_presidente} é o candidato {lista_Candidatos_Presidente[voto_presidente]} do partido {Partidos_Presidente[voto_presidente]}')
                    confirmacao = input('Deseja confirmar o voto: [Sim]/[Não]] ').upper()
                    if confirmacao == 'SIM':
                        Votos_Validos_Presidente[0] += 1

                        # Executa/Confirma o voto para o candidato selecionado
                        for i in range(len(lista_Candidatos_Presidente)):
                            if lista_Candidatos_Presidente[i] == lista_Voto_Presidente[i]:
                                lista_Voto_Presidente.remove(lista_Candidatos_Presidente[i])
                                lista_Voto_Presidente.insert(i, [lista_Candidatos_Presidente[i], i, Partidos_Presidente[i],'PRESIDENTE', 0])
                            if lista_Voto_Presidente[i][0] == lista_Candidatos_Presidente[voto_presidente]:
                                lista_Voto_Presidente[i] = [lista_Candidatos_Presidente[i], i, Partidos_Presidente[i],'PRESIDENTE', lista_Voto_Presidente[i][4] + 1]
                            else:
                                lista_Voto_Presidente[i] = [lista_Candidatos_Presidente[i], i, Partidos_Presidente[i],'PRESIDENTE', lista_Voto_Presidente[i][4]]
                        print('Voto sendo adicionado')
                        sleep(2)
                        print('-' * 45)
                        break
                    elif confirmacao == 'NAO':
                        print('Voto cancelado')
                    else:
                        print('opção inválida, tente novamente')
                else:
                    print('Erro, digite um voto válido')
        else:
            print('Erro, o eleitor não foi cadastrado')
        break

# Apresenta os candidatos vencedores para cada cargos e um ranking ordenado do resultado da eleição (do mais votado para o menos votado) + alguns dados estatísticos
def Resultado():
    global lista_Voto_Presidente, lista_Voto_Governador, lista_Voto_Prefeito

    # Tabela - PRESIDENTE
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA PRESIDENTE                |')
    print('-' * 66)
    print('|    Nome    |   Partido   |  Total de votos  |  % votos válidos |')
    print('-' * 66)
    ranking_presidente = sorted(lista_Voto_Presidente, key=itemgetter(4), reverse=True)
    for count, (candidato, numero, partido, cargo, votos) in enumerate(ranking_presidente, start=1):
        print('|{:^11} |{:>9}    |{:>15,.2f}   |{:>15,.2f}   |   '.format(candidato, partido, votos, 100*votos/(Voto_Nulo_Presidente[0]+Voto_Branco_Presidente[0]+Votos_Validos_Presidente[0])))
        print('-'*66)
    print(f'| Total de votos = {Votos_Validos_Presidente[0]+Voto_Nulo_Presidente[0]+Voto_Branco_Presidente[0]}\t\t\t\t\t\t\t\t\t\t |')
    print(f'| Total de votos válidos = {Votos_Validos_Presidente[0]} e % {100*Votos_Validos_Presidente[0]/(Voto_Nulo_Presidente[0]+Voto_Branco_Presidente[0]+Votos_Validos_Presidente[0]):,.2f} do total\t\t\t\t\t |')
    print(f'| Total de votos brancos = {Voto_Branco_Presidente[0]} e % {100*Voto_Branco_Presidente[0]/(Voto_Nulo_Presidente[0]+Voto_Branco_Presidente[0]+Votos_Validos_Presidente[0]):,.2f} do total\t\t\t\t\t |')
    print(f'| Total de votos nulos = {Voto_Nulo_Presidente[0]} e % {100*Voto_Nulo_Presidente[0]/(Voto_Nulo_Presidente[0]+Voto_Branco_Presidente[0]+Votos_Validos_Presidente[0]):,.2f} do total\t\t\t\t\t |')
    print('-' * 66)
    print('\n')

    # Tabela - GOVERNADOR
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA GOVERNADOR                |')
    print('-' * 66)
    print('|    Nome    |   Partido   |  Total de votos  |  % votos válidos |')
    print('-' * 66)
    ranking_governador = sorted(lista_Voto_Governador, key=itemgetter(4), reverse=True)
    for count, (candidato, numero, partido, cargo, votos) in enumerate(ranking_governador, start=1):
        print('|{:^11} |{:>9}    |{:>15,.2f}   |{:>15,.2f}   |   '.format(candidato, partido, votos, 100 * votos / (Voto_Nulo_Governador[0] + Voto_Branco_Governador[0] + Votos_Validos_Governador[0])))
        print('-' * 66)
    print(f'| Total de votos = {Votos_Validos_Governador[0] + Voto_Nulo_Governador[0] + Voto_Branco_Governador[0]}\t\t\t\t\t\t\t\t\t\t |')
    print(f'| Total de votos válidos = {Votos_Validos_Governador[0]} e % {100 * Votos_Validos_Governador[0] / (Voto_Nulo_Governador[0] + Voto_Branco_Governador[0] + Votos_Validos_Governador[0]):,.2f} do total\t\t\t\t\t |')
    print(f'| Total de votos brancos = {Voto_Branco_Governador[0]} e % {100 * Voto_Branco_Governador[0] / (Voto_Nulo_Governador[0] + Voto_Branco_Governador[0] + Votos_Validos_Governador[0]):,.2f} do total\t\t\t\t\t |')
    print(f'| Total de votos nulos = {Voto_Nulo_Governador[0]} e % {100 * Voto_Nulo_Governador[0] / (Voto_Nulo_Governador[0] + Voto_Branco_Governador[0] + Votos_Validos_Governador[0]):,.2f} do total\t\t\t\t\t |')
    print('-' * 66)
    print('\n')

    # Tabela - PREFEITO
    print('-' * 66)
    print('|            RANKING DO RESULTADO PARA PREFEITO                  |')
    print('-' * 66)
    print('|    Nome    |   Partido   |  Total de votos  |  % votos válidos |')
    print('-' * 66)
    ranking_prefeito = sorted(lista_Voto_Prefeito, key=itemgetter(4), reverse=True)
    for count, (candidato, numero, partido, cargo, votos) in enumerate(ranking_prefeito, start=1):
        print('|{:^11} |{:>9}    |{:>15,.2f}   |{:>15,.2f}   |   '.format(candidato, partido, votos, 100 * votos / (Voto_Nulo_Prefeito[0] + Voto_Branco_Prefeito[0] + Votos_Validos_Prefeito[0])))
        print('-' * 66)
    print(f'| Total de votos = {Votos_Validos_Prefeito[0] + Voto_Nulo_Prefeito[0] + Voto_Branco_Prefeito[0]}\t\t\t\t\t\t\t\t\t\t |')
    print(f'| Total de votos válidos = {Votos_Validos_Prefeito[0]} e % {100 * Votos_Validos_Prefeito[0] / (Voto_Nulo_Prefeito[0] + Voto_Branco_Prefeito[0] + Votos_Validos_Prefeito[0]):,.2f} do total\t\t\t\t\t |')
    print(f'| Total de votos brancos = {Voto_Branco_Prefeito[0]} e % {100 * Voto_Branco_Prefeito[0] / (Voto_Nulo_Prefeito[0] + Voto_Branco_Prefeito[0] + Votos_Validos_Prefeito[0]):,.2f} do total\t\t\t\t\t |')
    print(f'| Total de votos nulos = {Voto_Nulo_Prefeito[0]} e % {100 * Voto_Nulo_Prefeito[0] / (Voto_Nulo_Prefeito[0] + Voto_Branco_Prefeito[0] + Votos_Validos_Prefeito[0]):,.2f} do total\t\t\t\t\t |')
    print('-'*66)

# Função que exibe qual partido elegeu mais políticos
def partido_mais_frequente(lista):
    partidos = [partido for _, _, partido, _, _ in lista]
    contador = Counter(partidos)
    partido = contador.most_common(1)[0][0]
    return partido

# Função que exibe qual partido elegeu menos políticos
def partido_menos_frequente(lista):
    partidos = [partido for _, _, partido, _, _ in lista]
    contador = Counter(partidos)
    partido = contador.most_common()[-1][0]
    return partido

# Exibe uma lista dos eleitores que votaram, ordenados por nome e verifica se a quantidade de eleitores bate com o total de votos que foram registrados na eleição (auditoria)
def Relatorio():
    global partido_mais_frequente, partido_menos_frequente, lista_eleitores
    lista_eleitores.sort()
    lista_eleitores_ordenada = lista_eleitores
    print('-'*66)
    print('{:^66}'.format('RELATÓRIO'))
    print('-'*66)
    print(f'Lista de eleitores que votaram: {lista_eleitores_ordenada}')
    print(f'O total de votos para um candidato é {Votos_Validos_Prefeito[0] + Voto_Nulo_Prefeito[0] + Voto_Branco_Prefeito[0]} e a quantidade de eleitores é {len(lista_eleitores)}')

    # Combinação de todas as listas de votos
    todas_listas = []
    todas_listas.extend(lista_Voto_Presidente)
    todas_listas.extend(lista_Voto_Governador)
    todas_listas.extend(lista_Voto_Prefeito)

    # Calculando o partido mais frequente
    partido_mais_frequente = partido_mais_frequente(todas_listas)

    # Calculando o partido menos frequente
    partido_menos_frequente = partido_menos_frequente(todas_listas)

    # Exibindo o resultado
    print(f'O partido mais frequente é {partido_mais_frequente}')
    print(f'O partido menos frquente é {partido_menos_frequente}')
