print("Ejercicio 1 examen primer parcial Maldonado")
print("Opción a, digite un número")
a = int(input())
print("Opción b, digite un número")
b = int(input())

aumento = 1
if a > b:
    while aumento <= a:
        b = b + aumento
        aumento += 1
        print(b)
    else:
        while aumento <= b:
            a = a * aumento
            aumento +=1
            print(a)