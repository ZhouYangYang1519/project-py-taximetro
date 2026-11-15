def user_loggage():
    print("Add your Loggage")
    print("Now See you Issue")
    print("Now See you Issue number")

###Fase 1################################################################################################
import time

# 1. Iniciar el viaje
def arrancar(ID_Clientes, ID_taxista):
    print("Viaje iniciado")
    print("Cliente:", ID_Clientes)
    print("Taxista:", ID_taxista)
    return True


# 2. Comprobar si el taxi está parado o está en movimiento
def is_moving(estado):
    if estado.lower() == "movimiento":
        return True
    elif estado.lower() == "parado":
        return False
    else:
        raise ValueError("Estado no válido")


# 3. Actualizar el importe acumulado
def cuenta_total(cuenta, estado, tiempo):
    if is_moving(estado):
        cuenta = cuenta + 0.05 *tiempo
    else:
        cuenta = cuenta + 0.02 *tiempo

    return cuenta



# 4. Gestionar un viaje completo
def gestionar_viaje(ID_Clientes, ID_taxista):
        cuenta = 0.0
        viaje_activo = arrancar(ID_Clientes, ID_taxista)

        estado = "parado"  # Estado inicial del vehículo
        inicio = time.time()

        
while viaje_activo:
    # Leer el nuevo estado solicitado por el conductor
    nuevo_estado = input("Introduce el estado (parado/movimiento): ").strip().lower()

    # Comprobar que el nuevo estado sea válido
    if nuevo_estado not in ("parado", "movimiento"):
        print("Estado no válido")
        continue

    # Calcular cuánto tiempo ha durado el estado anterior
    fin = time.time()
    tiempo = fin - inicio

    # Cobrar según el estado anterior
    cuenta = cuenta_total(cuenta, estado, tiempo)

    # Cambiar al nuevo estado
    estado = nuevo_estado
    inicio = fin

    print("Cuenta actual:", round(cuenta, 2), "€")

    accion = input("Pulsa ENTER para continuar o T para terminar: ")

    if accion.upper() == "T":
        # Cobrar también el último tramo antes de finalizar
        fin = time.time()
        tiempo = fin - inicio
        cuenta = cuenta_total(cuenta, estado, tiempo)
        viaje_activo = False

        print("Viaje finalizado")
        print("Cuenta final:", round(cuenta, 2), "€")
    



# 5. Programa principal
def main():
    ID_Clientes = input("Introduce ID del cliente: ")
    ID_taxista = input("Introduce ID del taxista: ")

    while True:   # Bucle externo: varias carreras
        gestionar_viaje(ID_Clientes, ID_taxista)

# 5. Ejecutar el programa
if __name__ == "__main__":
    main()
