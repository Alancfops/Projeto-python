clientes={

}

enter=False
def register_customer(escolha):
    while True:
        try:
            novo_cliente = input("Digite seu nome: ")
            
            if not novo_cliente.strip():
                raise ValueError
            
            nova_senha = input("Digite sua senha: ")
            if not nova_senha.strip():
                raise ValueError
            
            if novo_cliente not in clientes:
                clientes[novo_cliente] = nova_senha
                print("Cliente cadastrado com sucesso")
            else:
                print("Usuário já cadastrado")
            break
        except ValueError:
            print("ERRO!! Os espaços não podem estar em branco ")

def customer_login(escolha):
    while True:
        try:
            cliente = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            
            if not cliente.strip():
                raise ValueError
            
            if cliente in clientes and clientes[cliente] == senha:
                print("Cliente logado com sucesso, aproveite e bom apetite")
                return True

            else:
                print("Nome ou senha incorretos, tente novamente")
        except ValueError:
            pass
        return False