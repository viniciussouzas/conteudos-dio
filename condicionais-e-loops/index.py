#estrutura condicional 
def sacar(valor: float):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print(saldo - valor)

    print("Obrigado volte sempre!")

sacar(100)

def depositar(valor: float): 
    saldo = 0

    if valor > 0.0:
        print("deposito efetuado")
        saldo = saldo + valor
        print(saldo)

    #também existe elif
    elif valor == 0:
        print("valor nulo")
    else: 
        print("valor inválido")

    print("Obrigado volte sempre!")


depositar(0)

#if aninhado

def caixa(conta, valor: float):
    saldo = 500
    
    conta_normal = "normal"
    conta_universitaria = "universitaria"

    if conta == conta_normal:
        if saldo >= valor:
            print("Saque realizado")
        elif valor > saldo:
            print("saque realizado com cheque especial")
    elif conta == conta_universitaria:
        if saldo >= valor:
            print("Saque realizado")
        elif valor > saldo:
            print("saldo insuficiente")

        
caixa("normal", 300)
caixa("normal", 700)
caixa("universitaria", 300)
caixa("universitaria", 700)

#if ternario
conta = "normal"
saldo = 500
valor = 200

status = "Sucesso" if conta == "normal" and saldo > valor else "Falha" 
print(f"{status} ao realizar o saque")
