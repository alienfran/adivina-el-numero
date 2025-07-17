import random  #Importamos el módulo random para generar números aleatorios

#Para que el contador inicie desde 1
MINIMO = 1

#Seleccionar la dificultad del juego Facil es hasta 1o, Medio hasta 50 y difícil hasta 100
dificultad = input("Elige la dificultad (F,M,D): ")

#Para definir el rango de números del juego, dependiendo de la dificultad que seleccione el usuario
if dificultad == "F":
    maximo = 10
elif dificultad == "M":
    maximo = 50
elif dificultad == "D":
    maximo = 100
elif dificultad not in "DMF":
    print("Error, no se encontró la dificultad")
    maximo = 10    

   

#Generamos un número aleatorio entre MINIMO y MAXIMO
numero_azar = random.randint(MINIMO, maximo)

#Inicializamos el contador de intentos
intentos = 0

#Iniciamos un bucle que se repetirá hasta que el usuario acierte
while True:
    #Pedimos al usuario que introduzca un número para especificar rango
    intento_usuario = int(input(f"Introduce un número [{MINIMO}-{maximo}]: "))

    #Aumentamos el contador de intentos en 1
    intentos += 1

    #Comprobamos si el número ingresado es mayor que el número a adivinar
    if intento_usuario > numero_azar:
        print("Te pasaste! El número es más pequeño que " + str(intento_usuario))

    #Comprobamos si el número ingresado es menor que el número a adivinar
    elif intento_usuario < numero_azar:
        print("Te quedaste corto! El número es más grande que " + str(intento_usuario))

    #Si el número ingresado es igual al número a adivinar, salimos del bucle
    else:
        break

#Una vez fuera del bucle, mostramos mensaje de acierto
print("Acertaste! El número era " + str(numero_azar))

#Mostramos cuántos intentos le tomó al usuario acertar
print(f"Total de intentos: {intentos}")
