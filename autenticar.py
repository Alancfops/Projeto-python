from alterar import limpar_rapido
from alterar import limpar_terminal
clientes={

}

enter=False
def register_customer(escolha):
    while True:
        try:
            print("")
            novo_cliente = input("Digite seu nome: ")
            print("")
            
            if not novo_cliente.strip():
                raise ValueError
            
            nova_senha = input("Digite sua senha: ")
            if not nova_senha.strip():
                raise ValueError
            
            if novo_cliente not in clientes:
                print("")
                clientes[novo_cliente] = nova_senha
                print("Cliente cadastrado com sucesso")
                limpar_terminal()
            else:
                print("")
                print("Usuário já cadastrado")
                limpar_rapido()
            break
        except ValueError:
            print("")
            print("ERRO!! Os espaços não podem estar em branco ")

def customer_login(escolha):
    while True:
        try:
            print("")
            cliente = input("Digite seu nome: ")
            print("")
            if not cliente.strip():
                raise ValueError
            senha = input("Digite sua senha: ")
            if not senha.strip():
                raise ValueError
            
            if cliente in clientes and clientes[cliente] == senha:
                print("")
                print("Cliente logado com sucesso, aproveite e bom apetite")
                limpar_terminal()
                return True

            else:
                print("")
                print("Nome ou senha incorretos, tente novamente")
                print("")
                limpar_rapido()
        except ValueError:
            print("")
            print("ERRO!!! Tente novamente")
            limpar_terminal()
        return False