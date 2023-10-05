from autenticar import*
from cardapio import*
import os
import time

while True:
    print("Bem vindo a pizzaria Smile")
    print("="*100)
    print("Menu")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Fazer pedido")
    print("4 - Finalizar programa")


    while True:
        try:
            escolha = int(input("Digite a escolha desejada: "))
            if escolha not in [1, 2, 3, 4]:
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
            fazer_pedido(escolha)
        else:
            print("Erro: Cadastre-se primeiro")
    elif escolha == 4:
        print("Obrigado pela preferência")
        break
