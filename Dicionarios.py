#Chave - str,int , Valor - lista,int,float
tabela = {
    "Alface": 1.50,
    "Maça": 2.30,
    "Batata": 3.00,
    "Feijão": 5.20
}
print(tabela)

#Encontrar o valor de Alface
print(tabela["Alface"])

#Se (não) tiver Alface no dicionario - True or False
print("Alface" in tabela)
print("Alface" not in tabela)

#pop exclui item do dicionario
tabela.pop("Maça")
print(tabela)

#Adiciona item no dicionario
tabela["Cebola"] = 7.6
print(tabela)

#Lista com as chaves do dicionario
print(tabela.keys())

#Lista com os valores
print(tabela.values())

#Lista de tuplas(chave, valor)
print(tabela.items())

