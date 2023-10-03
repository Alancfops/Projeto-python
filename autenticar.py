clientes={

}
def register_customer(escolha):
    novo_cliente=input("Digite seu nome: ")
    nova_senha=input("Digite sua senha: ")
    if novo_cliente not in clientes:
        clientes[novo_cliente] = nova_senha
        print("Cliente cadatrado com sucesso")
    else:
        print("Usuario ja cadastrado")

def customer_login(escolha):
    cliente = input("Digite seu nome: ")
    senha = input("Digite sua senha: ") 
    if cliente in clientes and clientes[cliente]==senha:
        print("Cliente logado com sucesso, aproveite e bom apetite")
    else:
        print("Nome ou senha incorretos, tente novamente")    
