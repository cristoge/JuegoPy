from Dibujos import menu_db,escogerdb,adivina_numero,errordb,ganardb,es_menordb,es_mayordb,vidas5,perderdb,turno1, turno2,jugadores,j1correcto,j2correcto,j1win,j2win,agradecimiento
import random
def menu():
    """
    Faltan comentarios
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
    print(vidas5)
    while vidas > 0:
        try:
            print(adivina_numero)
            intento = int(input())
            if intento < 1 or intento > 100:
                print(errordb)
                continue
            if intento == numero_secreto:
                print(ganardb)
                return
            elif intento < numero_secreto:
                print(es_mayordb)
            else:
                print(es_menordb)
            vidas -= 1
        except ValueError:
            print(errordb)
    print(perderdb)


def modo_2_jugadores_con_vidas():
    print(jugadores)
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
                print(turno1)
            else:
                print(turno2)

            try:
                print(adivina_numero)
                intento = int(input())
                if intento < 1 or intento > 100:
                    print(errordb)
                    continue

                if intento == numero_secreto:
                    if turno_jugador1:
                        print(j1correcto)
                        rondas_ganadas_j1 += 1
                    else:
                        print(j2correcto)
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
        print(j1win)
    elif rondas_ganadas_j2 > rondas_ganadas_j1:
        print(j2win)
    


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
                print(agradecimiento)
                break
            else:
                print(errordb)
        except Exception as e:
            print(f"Ocurrió un error: {e}. Inténtalo de nuevo.")


if __name__ == "__main__":
    juego()
