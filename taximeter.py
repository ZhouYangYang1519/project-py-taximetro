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
    tarifa_movimiento = 0.05
    tarifa_parado = 0.02

    if is_moving(estado):
        cuenta = cuenta + tarifa_movimiento * tiempo
    else:
        cuenta = cuenta + tarifa_parado * tiempo

    return cuenta


# 4. Leer y validar el comando del conductor
def leer_comando():
    while True:
        comando = input("Introduce parado, movimiento o T para terminar: ").strip().lower()
        if comando in ("parado", "movimiento", "t"):
            return comando
        print("Comando no válido")


# 5. Gestionar un viaje completo
def gestionar_viaje(ID_Clientes, ID_taxista):
    cuenta = 0.0
    viaje_activo = arrancar(ID_Clientes, ID_taxista)

    estado = "parado"
    inicio = time.time()
    nuevo_estado = None

    while viaje_activo:
        # Leer el siguiente comando
        nuevo_estado = leer_comando()

        # Calcular el tiempo del estado anterior
        fin = time.time()
        tiempo = fin - inicio

        # Cobrar el tramo anterior
        cuenta = cuenta_total(cuenta, estado, tiempo)
        inicio = fin

        
        if nuevo_estado == "t":
            viaje_activo = False
        else:
            estado = nuevo_estado
            print("Estado actual:", estado)
            print("Cuenta actual:", round(cuenta, 2), "€")

    print("Viaje finalizado")
    print("Cuenta final:", f"{cuenta:.2f}", "€")


# Mostrar las instrucciones de uso
# Mostrar las instrucciones de uso
def mostrar_instrucciones():
    print("========== TAXÍMETRO ==========")
    print("Bienvenido al sistema.")
    print()
    print("INSTRUCCIONES:")
    print("1. Introduce el ID del taxista.")
    print("2. Introduce el ID del cliente.")
    print("3. Durante el viaje, introduce 'parado' o 'movimiento' según el estado del taxi.")
    print("4. Introduce 'T' para terminar el viaje.")
    print("5. La cuenta se actualizará según el tiempo transcurrido y el estado del taxi.")
    print("6. Al finalizar, introduce 'S' para otra carrera o 'N' para cerrar el programa.")
    print()
    print("TARIFAS:")
    print("- Parado: 0.02 €/segundo")
    print("- Movimiento: 0.05 €/segundo")
    print("================================")
    print()



# 6. Programa principal
def main():
    mostrar_instrucciones()  # Mostrar instrucciones al iniciar
    ID_taxista = input("Introduce ID del taxista: ")

    while True:
        ID_Clientes = input("Introduce ID del nuevo cliente: ")

        gestionar_viaje(ID_Clientes, ID_taxista)

        print("Carrera finalizada. Listo para otro servicio.")

        opcion = input("¿Iniciar otra carrera? (S/N): ").strip().lower()

        if opcion == "n":
            print("Taxímetro cerrado")
            break

# 7. Ejecutar el programa
if __name__ == "__main__":
    main()
