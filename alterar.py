import os
import time
def novo_valor(pedidos, cardapio):
    valor_total = 0.00

    for pedido in pedidos:
        quantidade = pedido["quantidade"]
        sabor = pedido["sabor"]
        tamanho = pedido["tamanho"]

        if sabor in cardapio:
            preco_pizza = cardapio[sabor]

            if tamanho == "p" or tamanho == "pequena":
                preco_pizza -= 5.00
            elif tamanho == "m" or tamanho == "media":
                preco_pizza = preco_pizza
            elif tamanho == "g" or tamanho == "grande":
                preco_pizza += 5.00

            valor_sabor = quantidade * preco_pizza
            valor_total += valor_sabor

    return valor_total

def edit_order(pedidos, cardapio):
    while True:
        limpar_terminal()
        print("="*100)
        print("")
        print("Pedidos:")
        print("")
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1}: Sabor: {pedido['sabor']}, Quantidade: {pedido['quantidade']}, Tamanho: {pedido['tamanho']}")

        print("")
        print("="*100)
        try:
            print("")
            pedido_numero = int(input("Digite o número do pedido que deseja alterar ou 0 para sair: "))
            print("")
            time.sleep(0.8)
            if pedido_numero == 0:
                break
            if pedido_numero < 1 or pedido_numero > len(pedidos):
                raise ValueError
            pedido = pedidos[pedido_numero - 1]
            print("")
            print(f"Editando pedido {pedido_numero}: Sabor: {pedido['sabor']}, Quantidade: {pedido['quantidade']}, Tamanho: {pedido['tamanho']}")
            time.sleep(0.6)
            print("")

            quantidade = int(input(f"Qual a nova quantidade de pizzas que deseja para {pedido['sabor']}? "))
            print("")
            time.sleep(0.4)
            tamanho = input(f"Digite o novo tamanho das pizzas de {pedido['sabor']} (P-Pequena, M-Media, G-Grande): ").lower()
            print("")
            print("Editando...")
            time.sleep(0.8)
            if tamanho not in ["p", "pequena", "m", "media", "g", "grande"]:
                raise ValueError

            pedido["quantidade"] = quantidade
            pedido["tamanho"] = tamanho

            print("")
            print("Pedido atualizado com sucesso!")
            time.sleep(0.4)
            valor_total = novo_valor(pedidos, cardapio)
            print("")
            print(f"Novo valor total do pedido: R${valor_total:.2f}")
            print("")
            time.sleep(0.5)
            limpar_terminal()

        except ValueError:
            print("")
            print("Número de pedido inválido ou entrada incorreta. Tente novamente.")
            limpar_rapido()

def delete_order(pedidos, cardapio):
    while True:
        print("="*100)
        print("")
        print("Pedidos:")
        print("")
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1}: Sabor: {pedido['sabor']}, Quantidade: {pedido['quantidade']}, Tamanho: {pedido['tamanho']}")
        print("")
        print("="*100)
        time.sleep(0.6)
        try:
            print("")
            pedido_numero = int(input("Digite o número do pedido que deseja deletar ou 0 para sair: "))
            print("")
            time.sleep(0.8)
            if pedido_numero == 0:
                break
            if pedido_numero < 1 or pedido_numero > len(pedidos):
                raise ValueError

            del pedidos[pedido_numero - 1]
            print("Pedido removido com sucesso!")
            print("")
            time.sleep(0.4)
            valor_total = novo_valor(pedidos, cardapio)
            print(f"Novo valor total do pedido: R${valor_total:.2f}")
            time.sleep(0.5)
            limpar_terminal()

        except ValueError:
            print("")
            print("Número de pedido inválido ou entrada incorreta. Tente novamente.")
            limpar_terminal()

#Limpar terminal
def limpar_terminal():
    time.sleep(1.4)
    if os.name=='posix':
        os.system('clear')
    elif os.name=='nt':
        os.system('cls') 
def limpar_rapido():
    time.sleep(0.7)
    if os.name=='posix':
        os.system('clear')
    elif os.name=='nt':
        os.system('cls')    