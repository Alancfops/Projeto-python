from autenticar import*
from cardapio import*
from alterar import*
import os
import time

print("Bem vindo a pizzaria Smile")
while True:
    print("="*100)
    print("Menu")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Fazer pedido")
    print("4 - Editar pedido")
    print("5 - Excluir pedido")
    print("6 - Finalizar programa")


    while True:
        try:
            escolha = int(input("Digite a escolha desejada: "))
            if escolha not in [1, 2, 3, 4, 5, 6]:
                raise ValueError
            break
        except ValueError:
            print("ERRO! Apenas as opções informadas")

    if escolha == 1:
        register_customer(escolha)
    elif escolha == 2:
        enter=customer_login(escolha)
    elif escolha == 3:
        if enter==True:
            make_a_wish(escolha)
        else:
            print("Erro: Cadastre-se primeiro")
    elif escolha ==4:
         edit_order(pedidos, cardapio)
    elif escolha == 5:
        delete_order(pedidos, cardapio)         
    elif escolha == 6:
        print("Obrigado pela preferência")
        break
