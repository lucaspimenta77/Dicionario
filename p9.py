#Crie uma função que retorne a pessoa mais nova do dicionário.

pessoas ={"Lucas": 20, "Gabriel":21, "Rafael":30, "Mateus":40}

def idade(dicionario):
    if not dicionario:
        return None
    menor_idade = min(dicionario.values())
    return menor_idade

menor_idade = idade(pessoas)
if menor_idade is not None:
    print(f"A maior idade das pessoas é: {menor_idade}")
else:
    print("Não há idades no dicionário.")
