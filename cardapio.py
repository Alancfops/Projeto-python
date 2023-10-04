pedidos = {}
cardapio = {
    "Bacon": 25.00,
    "Calabresa": 30.00,
    "Quatro Queijos": 25.00,
    "Frango com Catupiry": 26.00,
    "Portuguesa": 31.00,
    "Cartola": 29.00,
}

def fazer_pedido(escolha):
    while True:
        for pizza, preco in cardapio.items():
            print(f"{pizza}: R${preco:.2f}")
        
        sabor = input("Digite o sabor da pizza que deseja ou digite 'Finalizar' para sair: ")
        
        if sabor.lower == "finalizar":
            print("Pedido finalizado")
            print(pedidos)
            valor_total = sum(pedidos[sabor] * cardapio[sabor] for sabor in pedidos)
            print(f"Valor total do pedido: R${valor_total:.2f}")
            break
        
        if sabor in cardapio:
            quantidade = int(input(f"Quantas pizzas de {sabor} deseja?: "))
            
            
            if sabor in pedidos:
                pedidos[sabor] += quantidade
            else:
               pedidos[sabor] = quantidade
        else:
            print("Sabor fora do cardápio")





     
            