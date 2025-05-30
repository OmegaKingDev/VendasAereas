voos = {}
passageiros = {"nome":[], "CPF":[], "telefone":[]}

def Fvoos():
    Nvoos = int(input("insira quantos voos serão cadastrados: "))

    for i in range(1, Nvoos + 1):
        vooDados = []
        escala = [] 
        escalas = []
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
        voos[i] = vooDados
        print(voos)
        
    return voos, origem, destino, escalas, preco, escalas, escala

def Fvenda():
    res = "N"
    while res == "N":
        print(f"Código dos voos disponiveis: ")      
        for i in voos.keys():
            print(f"- {i}")
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
            print("Para seguir com a compra insira os dados abaixo:")
            nome = input("Nome e sobrenome: ")
            passageiros["nome"].append(nome)
            cpf = int(input("CPF: "))
            passageiros["CPF"].append(cpf)
            telefone = int(input("Telefone: "))
            passageiros["telefone"].append(telefone)
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
                parcela = int(input("deseja parcelar em quantas vezes? MAXIMO DE 24x\n"))
                valorFinal = voos["preço"][indice] / parcela
                print(f"perfeito!! sua viagem de {voos['origem'][indice]} para {voos['destino'][indice]} que custará {valorFinal:.02f}, sendo {parcela}x de {voos['preço'][indice]} foi agendada! Aproveite suas férias.")
            else:
                print(f"Parabéns! sua viagem de {voos['origem'][indice]} para {voos['destino'][indice]} por {voos['preço'][indice]} foi agendada! Aproveite suas férias.")

            return cpf, nome, telefone
      

Fvoos()
Fvenda()   
