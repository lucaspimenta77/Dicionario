#Crie uma função que receba um nome e uma nova idade como parâmetros e atualize a idade da pessoa correspondente no dicionário.

def nome_a(dicionario, nome, nova_idade):
    if nome in dicionario:
        dicionario[nome] = nova_idade
        print(f"Idade de {nome} atualizada para {nova_idade}")
    else:
        print(f"{nome} não encontrado no dicionario")


pessoas ={"Lucas": 20, "Gabriel":21, "Rafael":30, "Mateus":40}

nome_atualizar = input("Digite o nome da pessoa que deseja atualizar a idade: ")
nova_idade = int(input('Digite a nova idade: '))

nome_a(pessoas, nome_atualizar, nova_idade)

print(pessoas)

