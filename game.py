# Iniciando la aleatorización de las opciones del juego
import random


# Inicializando las variables para contar partidas, vitorias, derrotas y empates
partidas = 0
victorias = 0
empates = 0
derrotas = 0

#Definiendo la opción para jugar otra ronda
while True:

    # Definiendo las acciones del usuario y del juego
    accion_usuario = input("Seleccione una opción entre (piedra, papel o tijeras): \n")
    acciones = ["piedra", "papel", "tijeras"]
    accion_juego = random.choice(acciones)
    partidas += 1

    # Mostrando las acciones del juego y del jugador
    print(f"\n Elegiste {accion_usuario}, el juego eligió {accion_juego}.\n")

    #Definiendo las reglas del juego
    if accion_usuario == accion_juego:
        print(f"El juego y tú eligieron la misma opción {accion_usuario}. Es un empate")
        empates += 1
    elif accion_usuario == "piedra":
        if accion_juego == "tijeras":
            print("La piedra rompe las tijeras. Jugador gana")
            victorias += 1
        else:
            print("El papel envuelve a la piedra. Jugador pierde")
            derrotas +=1
    elif accion_usuario == "papel":
        if accion_juego == "piedra":
            print("El papel envuelve a la piedra. Jugador gana")
            victorias += 1
        else:
            print("Las tijeras cortan el papel. Jugador pierde")
            derrotas +=1
    elif accion_usuario == "tijeras":
        if accion_juego == "papel":
            print("Las tijeras cortan el papel. Jugador gana")
            victorias += 1
        else:
            print("La piedra rompe las tijeras. Jugador pierde")
            derrotas +=1

    #Mostrando resultados
    print(f"Se han jugado {partidas} partidas. {victorias} victoria(s), {derrotas} derrota(s) y {empates} empate(s) ")
    
    # Consultando si se juega otra ronda  
    jugar_de_nuevo = input("¿Jugar de nuevo? (s/n): ")
    
    if jugar_de_nuevo.lower() != "s":
        break
    