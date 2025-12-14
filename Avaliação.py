import json

# Tenta carregar tentativas salvas
try:
    with open("feedback.json", "r") as arquivo:
        feedback = json.load(arquivo)
except FileNotFoundError:
    feedback = []

# Função para salvar dados no JSON
def salvar_dados():
    with open("feedback.json", "w") as arquivo:
        json.dump(feedback, arquivo, indent=4)

# Função para registrar tentativa
def registrar_feedback():
    nome = input("Usuário (ou sair): ").strip()
    if nome.lower() == "sair":
        return False

    else:
        print()
        print("/n-----Avaliação-----")
        print("Digite como foi sua experiência?")
        print("1 - Muito Ruim")
        print("2 - Ruim")
        print("3 - Razoável")
        print("4 - Muito Bom")
        print("5 - Excelente")

    resposta = input("").strip()
    while acesso not in ["1", "2", "3", "4", "5"]:
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
    print("1 - Registrar avaliação")
    print("2 - Sair")
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "1":
        continuar = registrar_feedback()
        if continuar == False:
            break
    elif escolha == "#DESENVOLVEDOR#":
        mostrar_resultados()
    elif escolha == "2":
        break
    else:
        print("Opção inválida. Tente novamente.\n")

