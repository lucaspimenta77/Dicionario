# Crie uma função que receba um nome como parâmetro e retorne a idade da pessoa correspondente no dicionário.
def buscar_idade_por_nome(nome, pessoas):
    if nome in pessoas:
        return f"A idade de {nome} é {pessoas[nome]}"
    else:
        return "Nome não encontrado"


pessoas = {"Lucas": 20, "Gabriel": 21, "Rafael": 30, "Mateus": 40}
nome = input("Digite um nome: ")

if nome in pessoas:
    print(f"A idade de {nome} é {pessoas[nome]}")
else:
    print("Nome não encontrado")
