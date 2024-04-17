texto = ""
VOGAIS  = "AEIOU"

#Exemplo usando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() #Adiciona quebra de linha


#Exemplo com range
for numero in range(0,51,5):
    print(numero, end=" ")

