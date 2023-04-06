""""
VETORES2 - Faça um programa que carregue dois vetores, X e Y, com dez números inteiros cada um.
Considere que os números de cada vetor digital, X e Y, não podem estar repetidos. Calcule e mostre os
seguintes vetores resultantes:
a.	a união de X com Y (todos os elementos de X e os elementos de Y que não estejam em X)
b.	a diferença entre X e Y (todos os elementos de X que não existam em Y)
c.	a soma entre X e Y (soma de cada elemento de X com o elemento de mesma posição em Y)
d.	produto entre X e Y (multiplicação de cada elemento de X com o elemento de mesma posição em Y)
e.	a interseção entre X e Y (apenas os elementos que aparecem nos dois vetores)

"""
conjx = [0] * 10
conjy = [0] * 10

for i in range(10):
    print("Posicao: ", i)
    repete = True
    while repete:
        print("Digite um numero: ")
        novonumero = int(input())
        for j in range(10):
            if novonumero == conjx[j]:
                print("Numero duplicado")
                repete = True
                break
        if j == 9:
            repete = False
            print("Numero inserido")
            conjx[i] = novonumero

for i in range(10):
    print("Posicao: ", i)
    repete = True
    while repete:
        print("Digite um numero: ")
        novonumero = int(input())
        for j in range(10):
            if novonumero == conjy[j]:
                print("Numero duplicado")
                repete = True
                break
        if j == 9:
            repete = False
            print("Numero inserido")
            conjy[i] = novonumero
print("conjy: ", conjy)
# a união de X com Y (todos os elementos de X e os elementos de Y que não estejam em X)
uniao = [0] * 10
for i in range(10):
    uniao[i] = conjx[i]

proxlivre = 10
for i in range(10):  #i indexador do conjY
    achei = False
    for j in range(10):
        if conjy[i] == conjx[j]:
            achei = True
            break
    #if achei == False:
    if not achei:
        uniao[proxlivre] = conjy[i]
        proxlivre += 1
print(uniao)

##b.	a diferença entre X e Y (todos os 
# elementos de X que não achei em Y)
diff = [0] * 10
proxlivre = 0
for i in range(10): #i - indexador do X
    achei = False
    for j in range(10): #j - indexador do Y
        if conjx[i] == conjy[j]:
            achei = True
            break
    #if achei == False:
    if not achei:
        diff[proxlivre] = conjx[i]
        proxlivre += 1
print("Diferenca: ", diff)

#c.	a soma entre X e Y (soma de cada 
# elemento de X com o elemento 
# de mesma posição em Y)
soma = [0] * 10
for i in range(10):
    soma[i] = conjx[i] + conjy[i]
print("Soma: ", soma)

#d.	produto entre X e Y (multiplicação 
# de cada elemento de X com o elemento 
# de mesma posição em Y)
prod = [0] * 10
for i in range(10):
    prod[i] = conjx[i] * conjy[i]
print("Produto: ", prod)

#e.	a interseção entre X e Y (apenas os 
# elementos que aparecem nos dois vetores)🐰🐰🐰🥚🥚🥚
inter = [0] * 10
proxlivre = 0
for i in range(10): #i - indexador X
    for j in range(10): #j - indexador Y
        if conjx[i] == conjy[j]:
            inter[proxlivre] = conjx[i]
            proxlivre += 1
            break
print("interseção: ", inter)
