#operadores aritméticos
print(10 - 5 * 2)

print((10 - 5) * 2)

print(10 ** 2 * 2)

print(10 ** (2 * 2))

print(10 / 2 * 4)

#operadores de comparação
# - igualdade
print(10 == 10)

# - diferença
print(10 != 11)

# - maior que/ maior ou igual e vice versa (menor que/ menor ou igual) - Retorna boolean (true or false)
print(10 > 9)
print(10 >= 9)

#operadores de atribuição
# - atribuição simples
saldo = 500

# - atribuição com adição, subtração, multiplicação e divisão, módulo, exponenciação
saldo = 500
saldo += 200
saldo -= 100
saldo *= 2
saldo /= 5
saldo //= 5
saldo %= 20
saldo **= 2

#operadores lógicos
# - and
10 > 9 and 9 < 20 # true, todos os operadores de comparação precisam ser verdadeiros

# - or
10 > 9 or 9 > 20 # true, apenas um dos operadores de comparação precisa ser verdadeiro

# - not (negação)
not 100 > 500 #true, inverso do que é verdade

#operadores de identidade - são operadores utilizados para comparar se dois objetos testados ocupam a mesma posição na memória
curso = 'Curso de Python'
nome_curso = curso

value, limit = 200, 200

curso is nome_curso

curso is not nome_curso

value is limit 

#operadores de associação - operadores utilizados para verificar se um objeto está presente em uma sequência - não é case sensitive
"Python" in curso

saques = [10, 20]

30 in saques

45 not in saques

10 in saques