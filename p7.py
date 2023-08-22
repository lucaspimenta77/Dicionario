#Crie uma função que retorne a média das idades das pessoas no dicionário.
def media_idade(dicionario):
    if not dicionario:
        return 0
    soma_idade = sum(dicionario.values())
    media = soma_idade / len(dicionario)
    return media

pessoas ={"Lucas": 20, "Gabriel":21, "Rafael":30, "Mateus":40}

media_idade = media_idade(pessoas)
print(f'A media das idades das pessoas é {media_idade:.2f}')