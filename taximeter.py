def user_loggage():
    print("Add your Loggage")
    print("Now See you Issue")
    print("Now See you Issue number")

###Fase 1################################################################################################
import time
import logging
import csv
import json


logging.basicConfig(
    filename="taximetro.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

with open("config.json", "r", encoding="utf-8") as archivo:
    config = json.load(archivo)



# 1. Iniciar el viaje
def arrancar(ID_Clientes, ID_taxista):
    print("Viaje iniciado")
    logging.info("Viaje iniciado")
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
    tarifa_movimiento = config["tarifa_movimiento"]
    tarifa_parado = config["tarifa_parado"]

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
        logging.warning(f"Comando no válido: {comando}")




# 5. Gestionar un viaje completo
def gestionar_viaje(ID_Clientes, ID_taxista):
    cuenta = 0.0
    viaje_activo = arrancar(ID_Clientes, ID_taxista)

    estado = "parado"
    inicio_viaje = time.time()
    inicio = inicio_viaje
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
    fin_viaje = time.time()
    duracion = fin_viaje - inicio_viaje
    fecha = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(inicio_viaje))
    logging.info(f"Viaje finalizado. Importe: {cuenta:.2f} €")
    
    print("Cuenta final:", f"{cuenta:.2f}", "€")
    with open("historial.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if archivo.tell() == 0:
            escritor.writerow([
                "fecha",
                "id_cliente",
                "id_taxista",
                "duracion_segundos",
                "importe"
            ])

        escritor.writerow([
            fecha,
            ID_Clientes,
            ID_taxista,
            round(duracion, 2),
            round(cuenta, 2)
        ])





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
    print(f"- Parado: {config['tarifa_parado']:.2f} €/segundo")
    print(f"- Movimiento: {config['tarifa_movimiento']:.2f} €/segundo")
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
