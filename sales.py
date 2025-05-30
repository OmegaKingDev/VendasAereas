voos = {}
passageiros = {}

#"nome":[], "CPF":[], "telefone":[]
def Fvoos():
    Nvoos = int(input("insira quantos voos serão cadastrados: "))

    for i in range(1, Nvoos + 1):
        vooDados = []
        escala = [] 
        escalas = []
        vooCodigo = int(input("Insira o codigo do voo: "))
        origem = (input(f"digite a origem do voo N°{i}: "))
        destino = (input(f"\nInsira o destino do voo N°{i}: "))
        Infoescalas = int(input("\nInsira a quantidade de escalas: "))
        escala = []           
        vooDados.append(origem)
        vooDados.append(destino)
        vooDados.append(Infoescalas)
        if Infoescalas > 0:
            for b in range (Infoescalas):
                escala.append(input(f"insira o lugar da escala: "))
            escalas.append(escala)
            vooDados.append(escalas)    

        preco = float(input("\nInsira o preço da passagem: "))
        lugares = int(input("\nInsira a quantidade de lugares disponiveis: ")) 
        vooDados.append(preco)
        vooDados.append(lugares)
        voos[vooCodigo] = vooDados
        print(voos)
        
    return voos, origem, destino, escalas, preco, escalas, escala

def Fvenda():
    res = "N"
    while res == "N":
        if not voos:
            print("Não há voos disponiveis no momento\n")
            w = (input("(S) para voltar para o menu principal\n")).upper()  
            while w != "S":
                w = (input("Valor invalido! (S) para voltar para o menu principal\n")).upper()
            return #
                
        else:
            print(f"Código dos voos disponiveis: ")      
        for i in voos.keys():
            print(f"- {i}")
        b = input("Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
        while b not in ["C", "V"]:
            b = input("Escolha invalida! Deseja continuar ou voltar para o menu principal? (C para continuar) (V para voltar)\n").upper()
        if b == "V":
            return #
        else:
            indice = int(input("escolha o N° do voo para ver as informações: "))
            print("origem:", {voos[indice][0]})
            print("destino:", {voos[indice][1]})
            if voos[indice][2] == 0:
                print("Não há escala.")
                print("preço: R$",voos[indice][3])
                print("lugares:", voos[indice][4])
            else:
                print(f"escalas: {voos[indice][3]}")
                print("preço: R$",voos[indice][4])
                print("lugares:", voos[indice][5])

            res = input("\nDeseja comprar esta passagem? (S para seguir com a compra) (N para voltar)\n").upper()
            while res not in ["S", "N"]:
                print("letra invalida!")
                res = input("Quer voltar? (S/N)").upper()

            if res == "S":
                dados = []
                print("Para seguir com a compra insira os dados abaixo:")
                nome = input("Nome e sobrenome: ")
                cpf = int(input("CPF: "))
                telefone = int(input("Telefone: "))

                dados.append(nome)
                dados.append(telefone)
                passageiros[cpf] = dados

                print("\n Como deseja pagar?")
                print("1 - Credito")
                print("2 - debito")
                compra = int(input("Escolha o metodo de pagamento: "))
                while compra < 1 or compra > 2:
                    print("numero invalido!")
                    compra = int(input("Escolha o metodo de pagamento: "))
                print("insira os dados do cartão: ")
                m = input("Nome no cartão: ")
                n = input("numero: ")
                v = input("validade: ")
                c = input("codigo de segurança: ")
                if compra == 1:
                    if voos[indice][2] == 0:
                        parcela = int(input("deseja parcelar em quantas vezes? MAXIMO DE 24x\n"))
                        valorFinal = voos[indice][3]/ parcela
                        print(f"perfeito!! sua viagem de {voos[indice][0]} para {voos[indice][1]} que custará {valorFinal:.02f}, sendo {parcela}x de {voos[indice][3]} foi agendada! Aproveite suas férias.")
                else:
                    print(f"Parabéns! sua viagem de {voos[indice][0]} para {voos[indice][1]} por {voos[indice][4]} foi agendada! Aproveite suas férias.")
    return cpf, nome, telefone

def consultaP():
    a=0


    
loop = "N"
while loop == "N":
    print("---- MENU ----")
    print(f"1 - Cadastrar voo")
    print(f"2 - Consultar e comprar passagem")
    print(f"2 - Lista de passageiros")
    opcao = int(input("\nEscolha uma das opções acima: "))
    if opcao == 1:
        Fvoos()
    elif opcao == 2:
        Fvenda()
    elif opcao == 3:
        consultaP()
