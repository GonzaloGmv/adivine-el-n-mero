import random
numero = random.randrange(0, 99)
respuesta = int (input ('Escriba un número entre 0 y 99: '))
intentos = 1

while respuesta != numero:
    while respuesta < 0 or respuesta > 99:
        print ("Número no válido")
        respuesta = int (input('Escriba otro numero entre 0 y 99: '))
        intentos += 1
    if respuesta < numero:
            print("Te has quedado corto")
            respuesta = int (input('Escriba otro numero entre 0 y 99: '))
    else:
            print("Te has pasado")
            respuesta = int (input('Escriba otro numero entre 0 y 99: '))
    intentos += 1
else:
    print("Enhorabuema, lo has acertado")

print ("Lo has acertado en ", intentos, " intentos")