voos = {}
passageiros = {}

def Fvoos():
    Nvoos = int(input(f"\nInsira quantos voos serão cadastrados: "))

    for i in range(1, Nvoos + 1):
        vooDados = []
        escala = [] 
        escalas = []
        vooCodigo = int(input(f"\nInsira o codigo do voo N°{i}: "))
        while vooCodigo in voos:
            print(f"Código de voo já existe. Por favor, insira outro.")
            vooCodigo = int(input(f"Insira um novo código de voo: "))
        origem = (input(f"digite a origem do voo N°{i}: "))
        destino = (input(f"Insira o destino do voo N°{i}: "))
        Infoescalas = int(input(f"Insira a quantidade de escalas: "))
        passageirosC = 0
        escala = []           
        vooDados.append(origem)
        vooDados.append(destino)
        vooDados.append(Infoescalas)
        
        if Infoescalas > 0:
            for b in range (Infoescalas):
                escala.append(input(f"Insira o lugar da escala: "))
            escalas.append(escala)
            vooDados.append(escalas)    

        preco = float(input(f"Insira o preço da passagem: "))
        lugares = int(input(f"Insira a quantidade de lugares disponiveis: ")) 
        vooDados.append(preco)
        vooDados.append(lugares)
        vooDados.append(passageirosC)
        voos[vooCodigo] = vooDados
        print("\nVoos cadastrados:")
        for codigo, dados in voos.items():
            origem = dados[0]
            destino = dados[1]
            print(f"- {codigo} | {origem} --> {destino}")

        
    return voos, origem, destino, escalas, preco, escalas, escala

def Fvenda():
    indice = int(input(f"Escolha o N° do voo para ver as informações: "))
    while indice not in voos.keys():
        print(f"Esse codigo não existe!")
        indice = int(input(f"escolha o N° do voo para ver as informações: "))
    if voos[indice][2] == 0:
        print(f"origem: {voos[indice][0]}")
        print(f"destino: {voos[indice][1]}")
        print(f"Não há escala.")
        print(f"preço: R${voos[indice][3]}")
        print(f"lugares: {voos[indice][4]}")
        if voos[indice][4] == 0:
            print(f"Este voo já está lotado! Não é possivel comprá-lo")
            w = (input(f"(S) para voltar para o menu principal\n")).upper()  
            while w != "S":
                w = (input(f"Valor invalido! (S) para voltar para o menu principal\n")).upper()
            return
                
    else:
        print(f"origem: {voos[indice][0]}")
        print(f"destino: {voos[indice][1]}")
        print(f"escalas: {voos[indice][3]}")
        print(f"preço: R${voos[indice][4]}")
        print(f"lugares: {voos[indice][5]}")
        if voos[indice][5] == 0:
            print(f"Este voo já está lotado! Não é possivel comprá-lo")
            w = (input(f"(S) para voltar para o menu principal\n")).upper()  
            while w != "S":
                w = (input(f"Valor invalido! (S) para voltar para o menu principal\n")).upper()
            return

    res = input(f"\nDeseja comprar esta passagem? (S para seguir com a compra) (N para voltar)\n").upper()
    while res not in ["S", "N"]:
        print(f"letra invalida!")
        res = input(f"Deseja comprar esta passagem? (S para seguir com a compra) (N para voltar) (S/N)").upper()

    if res == "S":
        dados = []
        print(f"Para seguir com a compra insira os dados abaixo:")
        nome = input(f"Nome e sobrenome: ")
        cpf = int(input(f"CPF: "))
        while cpf in passageiros:
            print("CPF já cadastrado! Por favor, insira outro CPF.")
            cpf = int(input(f"CPF: "))
        telefone = int(input(f"Telefone: "))

        dados.append(nome)
        dados.append(telefone)
        passageiros[cpf] = dados

                    
        print(f"\n Como deseja pagar?")
        print(f"1 - Credito")
        print(f"2 - Debito")
        compra = int(input(f"Escolha o metodo de pagamento: "))
        while compra < 1 or compra > 2:
            print(f"Número inválido!")
            compra = int(input(f"Escolha o metodo de pagamento: "))
        print(f"Insira os dados do cartão: ")
        m = input(f"Nome no cartão: ")
        n = input(f"Número: ")
        v = input(f"Validade: ")
        c = input(f"Código de segurança: ")
        if compra == 1:
            if voos[indice][2] == 0:
                parcela = int(input(f"Deseja parcelar em quantas vezes? MAXIMO DE 24x\n"))
                while parcela > 24 or parcela < 1:
                    print("Valor invalido!")
                    parcela = int(input(f"Deseja parcelar em quantas vezes? MAXIMO DE 24x\n"))  
                valorFinal = voos[indice][3]/ parcela
                print(f"Sua viagem de {voos[indice][0]} para {voos[indice][1]} que custará R${valorFinal:.02f} (sendo {parcela}x de R${voos[indice][3]}) foi agendada! Aproveite o voo.")
                voos[indice][4] = voos[indice][4] - 1
                passageiros[cpf].append(indice)
                voos[indice][5] += 1

                    
            else:
                parcela = int(input(f"Deseja parcelar em quantas vezes? MAXIMO DE 24x\n"))
                while parcela > 24 or parcela < 1:
                    print("Valor invalido!")
                    parcela = int(input(f"Deseja parcelar em quantas vezes? MAXIMO DE 24x\n"))  
                valorFinal = voos[indice][4]/ parcela
                print(f"Sua viagem de {voos[indice][0]} para {voos[indice][1]} que custará R${valorFinal:.02f} (sendo {parcela}x de R${voos[indice][4]}) foi agendada! Aproveite o voo.")
                voos[indice][5] = voos[indice][5] - 1
                passageiros[cpf].append(indice)
                voos[indice][6] += 1


        elif voos[indice][2] == 0:
            print(f"Sua viagem de {voos[indice][0]} para {voos[indice][1]} por R${voos[indice][3]} foi agendada! Aproveite o voo.")
            voos[indice][4] = voos[indice][4] - 1
            passageiros[cpf].append(indice)
            voos[indice][5] += 1
        else:
            print(f"Sua viagem de {voos[indice][0]} para {voos[indice][1]} por R${voos[indice][4]} foi agendada! Aproveite o voo.")
            voos[indice][5] = voos[indice][5] - 1
            passageiros[cpf].append(indice)    
            voos[indice][6] += 1
    if res == "N":
        return 
    return cpf, nome, telefone


def vooC():
    if not voos:
        print(f"Não há voos disponiveis no momento\n")
        w = (input(f"(S) para voltar para o menu principal\n")).upper()  
        while w != "S":
            w = (input(f"Valor invalido! (S) para voltar para o menu principal\n")).upper()
        return
                
    else:
        print(f"Código dos voos cadastrados: ")      
    for i in voos.keys():
        print(f"- {i}")
    b = input(f"Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
    while b not in ["C", "V"]:
        b = input(f"Escolha invalida! Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
    if b == "V":
        return
    else:
        Fvenda()
        
def vooO():
    if not voos:
        print(f"Não há voos disponiveis no momento\n")
        w = (input(f"(S) para voltar para o menu principal\n")).upper()  
        while w != "S":
            w = (input(f"Valor invalido! (S) para voltar para o menu principal\n")).upper()
        return

    origemBusca = input("Digite a origem desejada: ")
    encontrados = []
    for codigo, dados in voos.items():
        if dados[0] == origemBusca:
            print(f"- Código: {codigo} | Origem: {dados[0]} | Destino: {dados[1]}")
            encontrados.append(codigo)

    if not encontrados:
        print("Nenhum voo encontrado com esta origem.")
        w = (input(f"(S) para voltar para o menu principal\n")).upper()  
        while w != "S":
            w = (input(f"Valor invalido! (S) para voltar para o menu principal\n")).upper()
        return

    b = input(f"Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
    while b not in ["C", "V"]:
        b = input(f"Escolha invalida! Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
    if b == "V":
        return
    else:
        Fvenda()


def vooD():
    if not voos:
        print(f"Não há voos disponiveis no momento\n")  
        while w != "S":
            w = (input(f"Valor invalido! (S) para voltar para o menu principal\n")).upper()
        return

    destinoBusca = input("Digite o destino desejado: ")
    encontrados = []
    for codigo, dados in voos.items():
        if dados[1] == destinoBusca:
            print(f"- Código: {codigo} | Origem: {dados[0]} | Destino: {dados[1]}")
            encontrados.append(codigo)

    if not encontrados:
        print("Nenhum voo encontrado com este destino.")
        w = (input(f"(S) para voltar para o menu principal\n")).upper()  
        while w != "S":
            w = (input(f"Valor invalido! (S) para voltar para o menu principal\n")).upper()
        return

    b = input(f"Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
    while b not in ["C", "V"]:
        b = input(f"Escolha invalida! Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
    if b == "V":
        return
    else:
        Fvenda()


def consultaP():
    encontrados = False
    if not voos:
        print(f"Não há voos disponiveis no momento\n")
        w = (input(f"(S) para voltar para o menu principal\n")).upper()  
        while w != "S":
            w = (input(f"Valor invalido! (S) para voltar para o menu principal\n")).upper()
        return               
    else:
        print(f"Código dos voos cadastrados: ")      
    for i in voos.keys():
        print(f"- {i}")
    b = input(f"Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
    while b not in ["C", "V"]:
        b = input(f"Escolha inválida! Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
    if b == "V":
        return
    else:
        indice = int(input(f"Escolha o N° do voo para ver os passageiros: "))
        while indice not in voos.keys():
            print(f"Esse codigo não existe!")
            indice = int(input(f"Escolha o N° do voo para ver as informações: "))
    while indice not in voos.keys():
        print(f"Esse código não existe!")
        indice = int(input(f"Escolha o N° do voo para ver os passageiros: "))
    
    print(f"\nPassageiros do voo {indice}:")

    for cpf, x in passageiros.items():
        if indice in x:
            print(f"- CPF: {cpf} | Nome: {x[0]} | Telefone: {x[1]}")
            encontrados = True

    if not encontrados:
        print(f"Não há passageiros neste voo.")
        return
    else:
        p = input(f"Deseja cancelar uma passagem? (S/N)").upper()
        while p not in ["S","N"]:
            p = input(f"Escolha invalida! Deseja cancelar uma passagem? (S/N)").upper()


    if p == "S":
        cpf = int(input(f"Digite o CPF do passageiro que irá ter a passagem cancelada: "))

        while cpf not in passageiros:
            print(f"Passageiro não encontrado.")
            cpf = int(input(f"Digite o CPF do passageiro que irá ter a passagem cancelada: "))
        passageiros[cpf].remove(indice)
        if voos[indice][2] == 0:
            voos[indice][4] += 1
            print(f"Passagem cancelada")
            return
        else:
            voos[indice][5] += 1
            print(f"Passagem cancelada")
            return

def vooM():
    if not voos:
        print("Não há voos cadastrados.")
        return

    origemBusca = input("Digite a origem desejada: ")
    destinoBusca = input("Digite o destino desejado: ")

    menorEscala = -1
    codigoMenorEscala = -1

    for i in voos:
        voo = voos[i]
        origem = voo[0]
        destino = voo[1]
        escalas = voo[2]

        if origem == origemBusca and destino == destinoBusca:
            if menorEscala == -1 or escalas < menorEscala:
                menorEscala = escalas
                codigoMenorEscala = i

    if codigoMenorEscala == -1:
        print("Nenhum voo encontrado com essa origem e destino.")
        return

    voo = voos[codigoMenorEscala]
    print(f"\nVoo {codigoMenorEscala}")
    print(f"Origem: {voo[0]}")
    print(f"Destino: {voo[1]}")

    if voo[2] == 0:
        print(f"Preço: R${voo[3]}")
        print(f"Lugares: {voo[4]}")
    else:
        print(f"Escalas: {voo[3]}")
        print(f"Preço: R${voo[4]}")
        print(f"Lugares: {voo[5]}")
    
loop = "N"
while loop == "N":
    print(f"\n--------------- MENU ---------------")
    print(f"1 - Cadastrar voo")
    print(f"2 - Consultar e vender passagem")
    print(f"3 - Voo com menor escala")
    print(f"4 - Listagem de passageiros e cancelamento de passagem")
    opcao = int(input("\nEscolha uma das opções acima: "))
    if opcao == 1:
        Fvoos()
    elif opcao == 2:
        op = int(input("\n- 1 consutar voo pelo codigo\n- 2 consultar voo por origem\n- 3 consultar voo por destino\n"))
        while op not in [1, 2 ,3]:
            print("Valor invalido! tente novamente.")
            op = int(input("\n- 1 consutar voo pelo codigo\n- 2 consultar voo por origem\n- 3 consultar voo por destino\n"))
        if op == 1:
            vooC()
        elif op == 2:
            vooO()
        else:
            vooD()
    elif opcao == 3:
        vooM()
    elif opcao == 4:
        consultaP()