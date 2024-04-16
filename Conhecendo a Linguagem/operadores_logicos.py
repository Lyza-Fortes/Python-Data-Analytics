
# Converta a entrada para float, pois o valor do saque pode ser decimal
saque = float(input("Valor de saque: "))  

saldo = 1000
limite = 200
conta_especial = True

if saldo >= saque and saque <= limite or conta_especial and saldo >= saque:
    print("Transação autorizada", end='')  
else:
    print("Transação não autorizada")