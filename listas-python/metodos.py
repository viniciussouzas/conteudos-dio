#append

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

#clear
lista1 = [1, "Python", [40, 30, 20]]

print(lista1)  # [1, "Python", [40, 30, 20]]

lista1.clear()

print(lista1)

#copy
lista2 = [1, "Python", [40, 30, 20]]

lista2.copy()

print(lista2)  # [1, "Python", [40, 30, 20]]

#count
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

#extend
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

#index
linguagens1 = ["python", "js", "java"]

print(linguagens1.index("java")) #2

#pop (remove da lista)
linguagens2 = ["python", "js", "java"]

print(linguagens2.pop()) # java
print(linguagens2.pop()) # js
print(linguagens2.pop(0)) # python

#remove (também remove, mas passa o obj ao inves do index, retira apenas a primeira ocorrência)
linguagens3 = ["python", "js", "java"]
print(linguagens2.remove("js"))

#reverse
linguagens3 = ["python", "js", "java"]

linguagens3.reverse()
print(linguagens3)

#sort ou sorted
linguagens4 = ["python", "js", "c", "java", "csharp"]
linguagens4.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens4)

linguagens5 = ["python", "js", "c", "java", "csharp"]
linguagens5.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens5)

 #ordena por tamanho da string, do menor pro maior
linguagens6 = ["python", "js", "c", "java", "csharp"]
linguagens6.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens6)

linguagens7 = ["python", "js", "c", "java", "csharp"]
linguagens7.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens7)

linguagens8 = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens8))
print(sorted(linguagens8, key=lambda x: len(x)))

#len (tamanho dos elementos)
linguagens9 = ["python", "js", "c", "java", "csharp"]

print(len(linguagens9))  # 5
