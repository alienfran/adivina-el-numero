import random #ya que necesitamos obtener el número al azar

MINIMO = 1    #definir rango de números, en este caso del 1 al 10
MAXIMO = 10

numero_azar = random. randint(MINIMO, MAXIMO) #generar número al azar dentro de un rango, entre a y b 

while True:
    intento_usuario = int(input("Introduce un número")) #para solicitar al usuario que ingrese un número
    if numero_azar != intento_usuario: #para verificar si el numero coincide con el ingresado por el usuario
        print("Fallaste")              #si el número no coincide, se va a mostrar el mensaje "Fallaste"
    else:
        print("Acertaste")             #Si el número coincide, se va a mostrar el mensaje "Acertaste"
    break                            #para terminar proceso


