print("Ejercicio 1 examen primer parcial Maldonado")
print("Opcion a")
a=int(input())
print("Opcion b")
b=int(input())
aumento=1
if a > b:
    while aumento <= a:
        b = b + aumento
        aumento += 1
        
print(b)
if a > b:
    while aumento <= a:
        b = b * aumento
        aumento *= 1
        

