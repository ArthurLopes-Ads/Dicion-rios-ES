#Dicionario vazio
d = {}
d = dict()

#Cria um par chave e valor, chave - letra, valor - quantas vezes a letra aparece
for letra in "estrutura":
    d[letra] = d.get(letra, 0) + 1
print(d)