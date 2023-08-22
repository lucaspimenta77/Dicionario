#Crie uma função que remova uma pessoa do dicionário.

pessoas ={"Lucas": 20, "Gabriel":21, "Rafael":30, "Mateus":40}

def remover_pessoa(dicionario, nome):
    if nome in dicionario:
        del dicionario[nome]
        print(f'{nome} foi removido do dicionario.')
    else:
        print(f'{nome} não foi encontrado no dicionario.')

nome_a_remover = input("Digite um nome para remover do dicionario: ")
remover_pessoa(pessoas, nome_a_remover)
print(pessoas)  