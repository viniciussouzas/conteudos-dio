print('Hello world')

#váriaveis
name, age = ('Vinícius', 20)

print(f'meu nome é {name} e tenho {age} anos')

#constantes
FULLNAME = 'Vinícius Souza'
print(FULLNAME)

#convertendo tipos
# - inteiro pra float
preço = 10
preço = float(preço)
print(preço)
print(preço / 2)

# - float pra inteiro
valor = 10.30
valor = int(valor)
print(valor)
print(valor // 2)

# - numerico pra string
idade = 20
print(str(idade))
print(f"A váriavel idade apesar de ser de tipo numérico, quando chamada dessa maneira: {idade}, possui o tipo string")

# - string pra numero
nota = '10'
nota = int(nota)

#função builtin input - utilizada pra ler dados da entrada padrão
nome = input("informe seu nome: ")

#função builtin print - utilizada para exibir dados
print(nome)