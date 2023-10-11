from autenticar import*
from cardapio import*
from alterar import*
import os
import time

#Main da pizzaria
print("="*100)
print("")
print("Bem vindo a pizzaria Smile's")
print("")
while True:
    print("="*100)
    print("")
    print("Pizzaria Smile's")
    print("")
    print("Menu")
    print("")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Fazer pedido")
    print("4 - Editar pedido")
    print("5 - Excluir pedido")
    print("6 - Finalizar programa")


    while True:
        try:
            print("")
            escolha = int(input("Digite a escolha desejada: "))
            if escolha not in [1, 2, 3, 4, 5, 6]:
                raise ValueError
            break
        except ValueError:
            print("")
            print("ERRO! Apenas as opções informadas")

    if escolha == 1:
        register_customer(escolha)
    elif escolha == 2:
        enter=customer_login(escolha)
    elif escolha == 3:
        if enter==True:
            limpar_rapido()
            make_a_wish(escolha)
        else:
            print("")
            print("Erro: Cadastre-se primeiro")
            limpar_rapido()
    elif escolha ==4:
        edit_order(pedidos, cardapio)
        limpar_terminal()
    elif escolha == 5:
        delete_order(pedidos, cardapio)      
        limpar_terminal()       
    elif escolha == 6:
        print("")
        print("Finalizando...")
        time.sleep(0.8)
        limpar_terminal()
        print("="*100)
        print("")
        print("Obrigado pela preferência")
        print("")
        print("="*100)
        break
