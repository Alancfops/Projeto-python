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
        print("Pedidos:")
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1}: Sabor: {pedido['sabor']}, Quantidade: {pedido['quantidade']}, Tamanho: {pedido['tamanho']}")

        try:
            pedido_numero = int(input("Digite o número do pedido que deseja alterar ou 0 para sair: "))
            if pedido_numero == 0:
                break
            if pedido_numero < 1 or pedido_numero > len(pedidos):
                raise ValueError
            pedido = pedidos[pedido_numero - 1]
            print(f"Editando pedido {pedido_numero}: Sabor: {pedido['sabor']}, Quantidade: {pedido['quantidade']}, Tamanho: {pedido['tamanho']}")

            quantidade = int(input(f"Qual a nova quantidade de pizzas que deseja para {pedido['sabor']}? "))
            tamanho = input(f"Digite o novo tamanho das pizzas de {pedido['sabor']} (P-Pequena, M-Media, G-Grande): ").lower()

            if tamanho not in ["p", "pequena", "m", "media", "g", "grande"]:
                raise ValueError

            pedido["quantidade"] = quantidade
            pedido["tamanho"] = tamanho

            print("Pedido atualizado com sucesso!")

            valor_total = novo_valor(pedidos, cardapio)
            print(f"Novo valor total do pedido: R${valor_total:.2f}")

        except ValueError:
            print("Número de pedido inválido ou entrada incorreta. Tente novamente.")

def delete_order(pedidos, cardapio):
    while True:
        print("Pedidos:")
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1}: Sabor: {pedido['sabor']}, Quantidade: {pedido['quantidade']}, Tamanho: {pedido['tamanho']}")

        try:
            pedido_numero = int(input("Digite o número do pedido que deseja deletar ou 0 para sair: "))
            if pedido_numero == 0:
                break
            if pedido_numero < 1 or pedido_numero > len(pedidos):
                raise ValueError

            del pedidos[pedido_numero - 1]
            
            print("Pedido removido com sucesso!")

            valor_total = novo_valor(pedidos, cardapio)
            print(f"Novo valor total do pedido: R${valor_total:.2f}")

        except ValueError:
            print("Número de pedido inválido ou entrada incorreta. Tente novamente.")







