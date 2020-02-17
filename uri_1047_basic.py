h1 = int(input("hora inicio"))
m1 = int(input("minuto início"))
h2 = int(input("hora final"))
m2 = int(input("minuto final"))
horas = 0
minutos = 0

inicio = h1*60 + m1
final = h2*60 + m2

total = final - inicio
if total == 0:
    horas = 24
    minutos = 0

else:
    horas = total/60
    minutos = total % 60

print("O jogo durou ", int(horas), "horas e ", minutos, "minutos")
