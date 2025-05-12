voos = {"numero":[], "origem":[], "destino":[], "escalas":[], "preço":[], "lugares":[]}
passageiros = {"nome":[], "CPF":[], "telefone":[]}

def Fvoos():
    Nvoos = int(input("insira quantos voos serão cadastrados: "))

    for i in range(1, Nvoos + 1):
        voos["numero"].append(i)
        origem = (input(f"digite a origem do voo N°{i}: "))
        voos["origem"].append(origem)
        destino = (input(f"\nInsira o destino do voo N°{i}: "))
        voos["destino"].append(destino)
        escalas = int(input("\nInsira a quantidade de escalas: "))
        voos["escalas"].append(escalas)
        preco = float(input("\nInsira o preço da passagem: "))
        voos["preço"].append(preco)
        lugares = int(input("\nInsira a quantidade de lugares disponiveis: "))
        voos["lugares"].append(lugares)
    return voos, origem, destino, escalas, preco

def Fvenda():
    res = "N"
    while res == "N":
        print(voos["numero"])
        indice = int(input("escolha o N° do voo para ver as informações: "))
        indice -=1
        print("origem:", voos["origem"][indice])
        print("destino:", voos["destino"][indice])
        print("escalas:", voos["escalas"][indice])
        print("preço: R$",voos["preço"][indice])
        print("lugares:", voos["lugares"][indice])

        res = input("\nDeseja comprar esta passagem? (S para seguir com a compra) (N para voltar)").upper()
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
                print(f"perfeito!! sua viagem de {voos['destino'][indice]} para {voos['lugares'][indice]} que custará {valorFinal:.02f}, sendo {parcela}x de {voos["preço"][indice]} foi agendada! Aproveite suas férias.")
            else:
                print(f"Parabéns! sua viagem de {voos['destino'][indice]} para {voos['lugares'][indice]} por {voos['preço'][indice]} foi agendada! Aproveite suas férias.")

            return cpf, nome, telefone
      

Fvoos()
Fvenda()   
