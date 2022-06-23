print("Ejercicio 2 examen primer parcial Maldonado")
print("Seleccione una bebida")
opcion = input ()
if opcion == "A" or "a":
    a= 270
    while a <=270:
        print(a)
        a = a + 1
else:
    opcion == "B" or "b":
    b= 340
    while b <=340:
        print(b)
        b = b  + 1
else:
    opcion == "C" or "c":
    c= 390
    while c <=390:
        print(c)
        c = c  + 1

print("Ingrese monedas de 10, 50 o 100")

moneda = input()
suma = 1
if moneda == 10 or moneda == 50 or moneda == 100:
    suma = suma + moneda

if moneda == "10":
    moneda= 10
    while moneda <=10:
        suma = 10 + 1
else:
    moneda == "50":
    moneda= 50
    while moneda <=50:
        suma = 50  + 1
else:
    moneda == "100":
    moneda= 100
    while moneda <=100:
        suma = 100 + 1