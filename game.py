import random

accion_usuario = input("Seleccione una opción entre (piedra, papel o tijeras): \n")
acciones = ["piedra", "papel", "tijeras"]
accion_sistema = random.choice(acciones)

print(f"\n Elegiste {accion_usuario}, el juego eligió {accion_sistema}.\n")