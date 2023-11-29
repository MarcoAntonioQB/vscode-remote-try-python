# Iniciando la aleatorización de las opciones del juego
import random

# Definiendo las acciones del usuario y del juego
accion_usuario = input("Seleccione una opción entre (piedra, papel o tijeras): \n")
acciones = ["piedra", "papel", "tijeras"]
accion_juego = random.choice(acciones)

# Mostrando las acciones del juego y del jugador
print(f"\n Elegiste {accion_usuario}, el juego eligió {accion_juego}.\n")

if accion_usuario == accion_juego:
    print(f"El juego y tú eligieron la misma opción {accion_usuario}. Es un empate")
elif accion_usuario == "piedra":
    if accion_juego == "tijeras":
        print("La piedra rompe las tijeras. Jugador gana")
    else:
        print("El papel cubre a la piedra. Jugador pierde")
elif accion_usuario == "papel":
    if accion_juego == "piedra":
        print("El papel cubre a la piedra. Jugador gana")
    else:
        print("Las tijeras cortan el papel. Jugador pierde")
elif accion_usuario == "tijeras":
    if accion_juego == "papel":
        print("Las tijeras cortan el papel. Jugador gana")
    else:
        print("La piedra rompe las tijeras. Jugador pierde")
