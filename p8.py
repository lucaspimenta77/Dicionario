#Crie uma função que retorne a pessoa mais velha do dicionário.


pessoas ={"Lucas": 20, "Gabriel":21, "Rafael":30, "Mateus":40}

def idade(dicionario):
    if not dicionario:
        return None
    maior_idade = max(dicionario.values())
    return maior_idade

maior_idade = idade(pessoas)
if maior_idade is not None:
    print(f"A maior idade das pessoas é: {maior_idade}")
else:
    print("Não há idades no dicionário.")
