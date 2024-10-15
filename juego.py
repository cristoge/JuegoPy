from Dibujos import menu_db,escogerdb,adivina_numero,errordb,ganardb,es_menordb,es_mayordb
import random
def menu():
    """
    Menu del juego que consta de 5 opciones, el modo 1 como dice es el modo en el
    que es hasta no se acaba hasta que el usuario gane, no hay vidas y tiene pistas.
    El modo 2 es el modo donde solo tiene 5 oportunidades para poder ganar, tiene
    las pistas porque sino seria demasiado dificil.
    El modo 3 es el modo 2 jugadores, como dice, al mejor de 3, con pistas,
    cada uno tiene el turno para poder acertar el suyo, es a un total de 3
    entonces quien gane 2 gana.
    El modo 4 es el de 2 jugadores y quien se acerque a al numero gana.
    """
    print(menu_db)
    print(escogerdb)
    opcion = input()
    return opcion


def modo_1_jugador_sin_vidas():
    numero_secreto = 3
    intentos = 0
    while True:
        try:
            print(adivina_numero)
            intento = int(input())
            if intento < 1 or intento > 100:
                print(errordb)
                continue
            intentos += 1
            if intento == numero_secreto:
                print(ganardb)
                break
            elif intento < numero_secreto:
                print(es_mayordb)
            else:
                print(es_menordb)
        except ValueError:
            print(errordb)

def modo_1_jugador_con_vidas():
    numero_secreto = random.randint(1, 100)
    vidas = 5
    while vidas > 0:
        try:
            intento = int(input(f"Adivina el número (te quedan {vidas} vidas): "))
            if intento < 1 or intento > 100:
                print(errordb)
                continue
            if intento == numero_secreto:
                print("¡Has ganado!")
                return
            elif intento < numero_secreto:
                print(es_mayordb)
            else:
                print(es_menordb)
            vidas -= 1
        except ValueError:
            print(errordb)
    print(f"Has perdido. El número secreto era {numero_secreto}.")


def modo_2_jugadores_con_vidas():
    print("Jugador 1 y Jugador 2")
    jugador1 = "Jugador 1"
    jugador2 = "Jugador 2"
    rondas = 3
    rondas_ganadas_j1 = 0
    rondas_ganadas_j2 = 0

    for ronda in range(1, rondas + 1):
        print(f"\nRonda {ronda}")
        numero_secreto = random.randint(1, 100)
        turno_jugador1 = True  # Comienza el jugador 1

        while True:
            if turno_jugador1:
                print("Turno de jugador1:")
            else:
                print("Turno de jugador2:")

            try:
                intento = int(input("Adivina el número (entre 1 y 100): "))
                if intento < 1 or intento > 100:
                    print(errordb)
                    continue

                if intento == numero_secreto:
                    if turno_jugador1:
                        print("¡jugador1 ha acertado el número!")
                        rondas_ganadas_j1 += 1
                    else:
                        print("¡jugador2 ha acertado el número!")
                        rondas_ganadas_j2 += 1
                    break
                elif intento < numero_secreto:
                    print(es_mayordb)
                else:
                    print(es_menordb)

            except ValueError:
                print(errordb)

            # Cambiar de turno
            turno_jugador1 = not turno_jugador1


    if rondas_ganadas_j1 > rondas_ganadas_j2:
        print(f"¡{jugador1} ha ganado el juego!")
    elif rondas_ganadas_j2 > rondas_ganadas_j1:
        print(f"¡{jugador2} ha ganado el juego!")
    
    print("\n¡Juego terminado!")


def modo_2_jugadores_quien_se_acerca_mas():
    jugador1 = 'jugador1'
    jugador2 = 'jugador2'
    numero_secreto = random.randint(1, 100)

    while True:
        try:
            intento_j1 = int(input(f"{jugador1}, adivina el número (entre 1 y 100): "))
            if intento_j1 < 1 or intento_j1 > 100:
                print("Por favor, introduce un número entre 1 y 100.")
                continue

            intento_j2 = int(input(f"{jugador2}, adivina el número (entre 1 y 100): "))
            if intento_j2 < 1 or intento_j2 > 100:
                print("Por favor, introduce un número entre 1 y 100.")
                continue

            break  # Salir del bucle si ambas entradas son válidas

        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    diferencia_j1 = abs(numero_secreto - intento_j1)
    diferencia_j2 = abs(numero_secreto - intento_j2)

    if diferencia_j1 < diferencia_j2:
        print("¡jugador1 ha ganado!")
    elif diferencia_j2 < diferencia_j1:
        print("¡jugador2 ha ganado!")
    else:
        print("Empate.")
    print(f'El numero era {numero_secreto}')

def juego():
    while True:
        try:
            opcion = menu()
            if opcion == "1":
                modo_1_jugador_sin_vidas()
            elif opcion == "2":
                modo_1_jugador_con_vidas()
            elif opcion == "3":
                modo_2_jugadores_con_vidas()
            elif opcion == "4":
                modo_2_jugadores_quien_se_acerca_mas()
            elif opcion == "5":
                print("Saliendo del juego...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error: {e}. Inténtalo de nuevo.")


if __name__ == "__main__":
    juego()
