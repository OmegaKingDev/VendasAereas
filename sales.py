voos = {"numero":[], "origem":[], "destino":[], "escalas":[], "preço":[], "lugares":[]}
passageiros = {"CPF":[], "nome":[],"telefone":[]}

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

def retornar():
    res = "S"
    while res == "S":
        print(voos["numero"])
        indice = int(input("escolha o N° do voo para ver as informações: "))
        indice -=1
        print("origem:", voos["origem"][indice])
        print("destino:", voos["destino"][indice])
        print("escalas:", voos["escalas"][indice])
        print("preço: R$",voos["preço"][indice])
        print("lugares:", voos["lugares"][indice])
        res = input("Quer voltar? (S/N)").upper()
        while res not in ["S", "N"]:
            print("letra invalida!")
            res = input("Quer voltar? (S/N)").upper()
            

Fvoos()   
retornar()