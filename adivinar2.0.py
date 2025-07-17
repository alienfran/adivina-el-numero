import random  #Importamos el módulo random para generar números aleatorios

#Definimos los valores mínimo y máximo del rango
MINIMO = 1     # Límite inferior del número a adivinar
MAXIMO = 10    # Límite superior del número a adivinar

#Generamos un número aleatorio entre MINIMO y MAXIMO
numero_azar = random.randint(MINIMO, MAXIMO)

#Inicializamos el contador de intentos
intentos = 0

#Iniciamos un bucle que se repetirá hasta que el usuario acierte
while True:
    #Pedimos al usuario que introduzca un número y lo convertimos a entero
    intento_usuario = int(input("Introduce un número: "))

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
print(f"Total de intentos: {intentos} ")
