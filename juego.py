import random
from Dibujos import *
def menu():
    """
    Aqui se ve el menu, donde se despliegan el menu de la carpeta Dibujos
    Donde hay 4 opciones.
    El modo 1 jugador, el modo un jugador dificil que consta de 5 intentos 
    y el modo 2 jugadores, mas adelante estan definidos.
    Todos los textos estan hecho con los dibujos y todo tiene su try catch
    para gestionar que no explote el programa.
    """
    print(menu_db)
    print(escogerdb)
    opcion = input()
    return opcion


def modo_1_jugador_sin_vidas():
    """
    Este modo es de un solo jugador, es infinito hasta que el usuario gane,
    Cuando selecciona un numero, sale si es mayor o es menor y 
    si es el numero gana.
    """
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            print(adivina_numero)
            intento = int(input())
            if intento < 1 or intento > 100: #gestion de error.
                print(errordb)
                continue # si hay un error se salta el ciclo.
            intentos += 1
            if intento == numero_secreto:
                print(ganardb)
                break
            elif intento < numero_secreto:
                print(es_mayordb)
            else:
                print(es_menordb)
        except ValueError: #gestion de error con su propio dibujo.
            print(errordb)

def modo_1_jugador_con_vidas():
    """
    Igual que le modo de un jugador solo que hay un total de 5 vidas.
    La logica la gestion todo es igual que el anterior.
    """
    numero_secreto = random.randint(1, 100)
    vidas = 5
    print(vidas5)
    while vidas > 0: #mientras haya vidas se ejecutara el ciclo.
        try:
            print(adivina_numero)
            intento = int(input())
            if intento < 1 or intento > 100: #mismo control de error que antes.
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
    """
    En este modo hay dos jugadores, se selecciona un numero aleatorio
    entonces el jugador 1 y el jugador 2 se turnan para adivinar el numero.
    Cada vez que se da un numero se dice si es mayor o menor o si es el numero.
    Hay un total de 3 rondas y el que gane mas pues gana.
    """
    print(jugadores)
    jugador1 = "Jugador 1" #se inicializan
    jugador2 = "Jugador 2"
    rondas = 3
    rondas_ganadas_j1 = 0
    rondas_ganadas_j2 = 0

    for ronda in range(1, rondas + 1):
        print(f"\nRonda {ronda}")
        numero_secreto = random.randint(1, 100)
        turno_jugador1 = True  # En este caso siempre empezara el jugador 1
        #En este caso el bucle se ejecuta al jugador 1
        #Si el numero se acierta y no lo ha adivinado el jugador1
        #la victoria seria del jugador 2.
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

            # En este caso se cambia de turno y el ciclo se repite
            turno_jugador1 = not turno_jugador1

#Saldra el mensaje de quien gana el juego.
    if rondas_ganadas_j1 > rondas_ganadas_j2:
        print(j1win)
    elif rondas_ganadas_j2 > rondas_ganadas_j1:
        print(j2win)



def juego():
    """
    Este es el juego, aqui inicia todo y dependiendo de la opcion
    que escoja el usuario se ejecutara una funcion o otra.
    En caso de querer salir marcara la opcion 4 y saldra un mensaje
    de Gracias por jugar.
    """
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

#función main para iniciar el juego.
if __name__ == "__main__":
    juego()
