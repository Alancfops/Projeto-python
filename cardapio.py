pedidos={}
cardapio = {
    "G-Bacon": 25.00,
    "G-Calabresa": 30.00,
    "G-Quatro Queijos": 25.00,
    "G-Frango com Catupiry": 26.00,
    "G-Portuguesa": 31.00,
    "G-Cartola": 29.00,
    }
def fazer_pedido(escolha):
     pedidos={}
     for pizza, preco in cardapio.items():
        print(f"{pizza}: R${preco:.2f}")
     sabor=input("Digite o sabor da pizza que deseja: ") \
     if sabor in cardapio:
     quantidade=input(f"Quantas pizzas de {sabor} deseja?: ")
     
     
            