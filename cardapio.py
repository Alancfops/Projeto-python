pedidos = {}
cardapio = {
    "bacon": 25.00,
    "calabresa": 30.00,
    "quatro queijos": 25.00,
    "frango com catupiry": 26.00,
    "portuguesa": 31.00,
    "cartola": 29.00,
}

def make_a_wish(escolha):
    while True:
        for pizza, preco in cardapio.items():
            print(f"{pizza}: R${preco:.2f}")

        try:
            sabor = input("Digite o sabor da pizza que deseja ou digite 'Finalizar' para sair: ").lower()
            
            if sabor == "finalizar":
                print("Pedido finalizado")
                print(pedidos)

                valor_total = 0.00

                for sabor, detalhes in pedidos.items():
                    quantidade = detalhes["quantidade"]
                    tamanho = detalhes["tamanho"]

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

                print(f"Valor total do pedido: R${valor_total:.2f}")
                break

            if sabor in cardapio:
                while True:
                    try:
                        quantidade = int(input(f"Quantas pizzas de {sabor} deseja?: "))
                        if quantidade < 1:
                            raise ValueError
                        break
                    except ValueError:
                        print("Quantidade inválida, digite um número maior que zero.")
                    
                while True:
                    try:
                        tamanho = input("Qual o tamanho das pizzas? (P-Pequena, M-Media, G-Grande): ").lower()
                            
                        if tamanho not in ["p", "pequena", "m", "media", "g", "grande"]:
                            raise ValueError
                        break
                    except ValueError:
                        print("Tamanho inválido")

                if sabor in pedidos:
                    pedidos[sabor]["quantidade"] += quantidade
                    pedidos[sabor]["tamanho"] = tamanho
                else:
                    pedidos[sabor] = {"quantidade": quantidade, "tamanho": tamanho}
            else:
                print("Sabor inexistente. Por favor, escolha um sabor válido.")
        
        except ValueError:
            print("ERRO!!!, Tente novamente")