
########## Manipulação de Strings ##########

nome = 'Lyza'
idade = '29'
profissao = 'Analista de dados'
linguagem = 'Python'
saldo = 45.548

#Dicionário
dados = {"nome": "Lyza", "idade": 28}

#Formato não muito utilizado (método format) 
print("Nome: %s, Idade: %s" % (nome, idade))
print("Nome: {}, Idade: {}" .format(nome, idade))
#Com indices
print("Nome: {1}, Idade: {0}" .format(nome, idade))
#Consigo passar quantas vezes vou utilizar
print("Nome: {1}, Idade: {0} Nome: {1} {1}" .format(nome, idade))


#Com dicionário:
print("Nome: {nome}, Idade: {idade}".format(**dados))

#f-string (mais utilizado)
print(f"Nome: {nome}, Idade {idade}")

print(f"Nome: {nome}, Idade {idade} Saldo: {saldo:1.2f}")

