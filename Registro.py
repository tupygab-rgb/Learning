import json

# Tenta carregar tentativas salvas
try:
    with open("tentativas.json", "r") as arquivo:
        tentativas = json.load(arquivo)
except FileNotFoundError:
    tentativas = []

# Função para salvar dados no JSON
def salvar_dados():
    with open("tentativas.json", "w") as arquivo:
        json.dump(tentativas, arquivo, indent=4)

# Função para registrar tentativa
def registrar_tentativa():
    nome = input("Usuário (ou sair): ").strip()
    if nome.lower() == "sair":
        return False

    acesso = input("Meu acesso foi (falha ou sucesso): ").lower().strip()
    while acesso not in ["falha", "sucesso"]:
        acesso = input("Digite apenas 'falha' ou 'sucesso': ").lower().strip()

    resultado = {"Usuário": nome, "Acesso foi": acesso}
    tentativas.append(resultado)
    salvar_dados()
    return True

# Função para mostrar resultados
def mostrar_resultados():
    falhas = 0
    sucessos = 0
    print("\n--- Resultados ---")
    for t in tentativas:
        if t["Acesso foi"] == "falha":
            print(f"Usuário {t['Usuário']} foi negado")
            falhas += 1
        elif t["Acesso foi"] == "sucesso":
            print(f"Usuário {t['Usuário']} foi liberado")
            sucessos += 1
    print("\nTotal de falhas:", falhas)
    print("Total de sucessos:", sucessos)
    print("------------------\n")

# Loop principal do menu
while True:
    print("1 - Registrar tentativa")
    print("2 - Mostrar resultados")
    print("3 - Sair")
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "1":
        continuar = registrar_tentativa()
        if continuar == False:
            break
    elif escolha == "2":
        mostrar_resultados()
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Tente novamente.\n")

