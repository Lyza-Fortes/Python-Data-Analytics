saldo = 300
saque = 250

status = "Sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")