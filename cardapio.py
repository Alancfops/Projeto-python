import time
from alterar import limpar_rapido
pedidos = [] 

cardapio = {
    "bacon": 25.00,
    "calabresa": 30.00,
    "queijo": 20.00,
    "frango": 20.00,
    "portuguesa": 31.00,
    "cartola": 29.00,
}

def make_a_wish(escolha):
    while True:
        print("="*100)
        print("")
        print("Pizza: ")
        print("")
        for pizza, preco in cardapio.items():
            print(f"{pizza}: R${preco:.2f}")

        try:
            print("="*100)
            print("")
            sabor = input("Digite o sabor da pizza que deseja ou digite 'Finalizar' para sair: ").lower()
            
            if sabor == "finalizar":
                print("")
                print("Pedido finalizado")
                print("")
                time.sleep(0.4)
                print("Pedidos:")
                for pedido in pedidos:
                    print("")
                    print(f"Sabor: {pedido['sabor']}, Quantidade: {pedido['quantidade']}, Tamanho: {pedido['tamanho']}")

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
                print("")
                print(f"Valor total do pedido: R${valor_total:.2f}")
                break

            if sabor in cardapio:
                while True:
                    try:
                        print("")
                        quantidade = int(input(f"Quantas pizzas de {sabor} deseja?: "))
                        if quantidade < 1:
                            raise ValueError
                        break
                    except ValueError:
                        print("")
                        print("Quantidade inválida, digite um número maior que zero.")
                    
                while True:
                    try:
                        print("")
                        tamanho = input("Qual o tamanho das pizzas? (P-Pequena, M-Media, G-Grande): ").lower()
                            
                        if tamanho not in ["p", "pequena", "m", "media", "g", "grande"]:
                            raise ValueError
                        break
                    except ValueError:
                        print("")
                        print("Tamanho inválido")

                pedido = {"sabor": sabor, "quantidade": quantidade, "tamanho": tamanho}
                
                pedidos.append(pedido)
            else:
                print("")
                print("Sabor inexistente. Por favor, escolha um sabor válido.")
        
        except ValueError:
            print("")
            print("ERRO!!!, Tente novamente")
            limpar_rapido()

           


