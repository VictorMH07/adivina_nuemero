import random


def juego_adivinanza():
    # generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intento = 0
    adivinado = False

    # Primera linea te da la bienvenida
    print("Bienvenido al juego de adivinanza de nuemro")
    print("Debes adivinar un numero entre el 1 al 100")
    print("¡Intenta adivinar!")

    while not adivinado:
        # Solicita un numero
        adivinanza = input("Introduzca el numero del 1 al 100: ")

        # verificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # lo estamos pasando de texto a entero
            intento += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones has ganado! el numero {adivinanza} es el secreto y lo has logrado en {intento} intentos"
                )
        else:
            print("Por favor introduce un numero valido del 1 al 100")


juego_adivinanza()
