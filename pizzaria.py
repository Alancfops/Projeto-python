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
    print("4 - Descontos disponiveis")
    print("5 - Finalizar pedido")

    escolha=int(input("Digite a escolha desejada: "))
    if escolha == 1:
        register_customer(escolha)
    elif escolha == 2:
        customer_login(escolha)   
    elif escolha == 3:
        fazer_pedido(escolha)  
    
