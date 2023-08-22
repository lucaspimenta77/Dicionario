#Crie uma função que retorne uma lista com as pessoas cujo nome começa com a letra "J".

pessoas ={"Lucas": 20, "Gabriel":21, "Rafael":30, "Mateus":40, "Joao":43, "Josias":23}

def letra_nome_pessoas(dicionario, letra):
    letra_no_nome = [nome for nome in dicionario if nome.startswith(letra)]
    return letra_no_nome

letra = "J"

pessoas_j = letra_nome_pessoas(pessoas, letra)
print(f"Pessoas cujo começa com '{letra}': {pessoas_j}")