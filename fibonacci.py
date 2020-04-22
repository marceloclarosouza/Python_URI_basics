#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

fib = int(input("Digite o numero de elementos da sequencia"))
ant1 = 1
ant2 = 1
prox = 0


for i in range(1,fib):## this code will return N numbers of the sequece
    if i <=2:
        print(ant1)
    else:
        prox = ant1 + ant2
        print(prox)
        ant1 = ant2
        ant2 = prox
        i+=1

i = 3
print(ant1)
print(ant2)
while i < fib:##this code prints up to the declared fib number
        prox = ant1 + ant2
        print(prox)
        ant2 = ant1
        ant1 = prox
        i = prox
