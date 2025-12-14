tentativas = []
sucessos = 0
falhas = 0 
def registrar_tentativa():
    nome = input("Usuário(ou sair):")
    if nome == "sair":
        return False
    else:
        acesso = input("Meu acesso foi(falha ou sucesso):") #fiquei em duvída se colocaria o return True já aqui ou não#
        if acesso == "falha":
            falhas += 1
        elif acesso == "sucesso":
            sucessos += 1
        resultado = {
        "Usuário": nome,
        "Acesso foi": acesso
        }
    
        tentativas.append(resultado)
        return True

def mostrar_resultados():
    print(tentativas)
    print("Total de falhas:", falhas)
    print("Total de sucessos:", sucessos)
    
     
