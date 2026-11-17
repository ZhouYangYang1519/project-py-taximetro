import json
import time
import csv
import logging


logging.basicConfig(
    filename="taximetro.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


########################################################################################################

class Taximetro:
    def __init__(self):
        self.cuenta = 0.0
        self.estado = "parado"
        self.viaje_activo = False
        self.inicio = None
        self.fin_viaje = None
        with open("config.json", "r", encoding="utf-8") as archivo:
            self.config = json.load(archivo)


    def iniciar_carrera(self):
        if self.viaje_activo:
            raise ValueError("Ya hay una carrera activa")
        self.cuenta = 0.0
        self.estado = "parado"
        self.viaje_activo = True
        self.inicio = time.time()
        self.fin_viaje = None

        print("Viaje iniciado")
        logging.info("Viaje iniciado")





    
    def finalizar_carrera(self):
        if not self.viaje_activo:
            raise ValueError("No hay ninguna carrera activa")
        fin = time.time()
        self.fin_viaje = fin
        tiempo = fin - self.inicio
        self.cuenta_total(tiempo)

        self.viaje_activo = False
        print("Viaje finalizado")
        print("Cuenta final:", f"{self.cuenta:.2f}", "€")
        logging.info(f"Viaje finalizado. Importe: {self.cuenta:.2f} €")

        return self.cuenta



    def is_moving(self):
        if self.estado.lower() == "movimiento":
            return True
        elif self.estado.lower() == "parado":
            return False
        else:
            raise ValueError("Estado no válido")

    def cuenta_total(self, tiempo):
        tarifa_movimiento = self.config["tarifa_movimiento"]
        tarifa_parado = self.config["tarifa_parado"]

        if self.is_moving():
            self.cuenta = self.cuenta + tarifa_movimiento * tiempo
        else:
            self.cuenta = self.cuenta + tarifa_parado * tiempo

        return self.cuenta


    def cambiar_estado(self, nuevo_estado):
        if not self.viaje_activo:
            raise ValueError("No hay ninguna carrera activa")

        if nuevo_estado not in ("parado", "movimiento"):
            logging.warning(f"Estado no válido: {nuevo_estado}")
            raise ValueError("Estado no válido")

        fin = time.time()
        tiempo = fin - self.inicio

        self.cuenta_total(tiempo)

        self.inicio = fin
        self.estado = nuevo_estado

        print("Estado actual:", self.estado)
        print("Cuenta actual:", f"{self.cuenta:.2f}", "€")
    

########################################################################################################

class Carrera:
    def __init__(self, id_cliente, id_taxista, inicio):
        self.id_cliente = id_cliente
        self.id_taxista = id_taxista
        self.inicio = inicio
        self.fin = None
        self.duracion_segundos = 0.0
        self.importe = 0.0


    
    def finalizar(self, importe, fin):
        self.fin = fin
        self.duracion_segundos = self.fin - self.inicio
        self.importe = importe




########################################################################################################
class Historial:
    def __init__(self, archivo="historial.csv"):
        self.archivo = archivo

    def guardar(self, carrera):
        with open(self.archivo, "a", newline="", encoding="utf-8") as archivo:
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
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(carrera.inicio)),
                carrera.id_cliente,
                carrera.id_taxista,
                round(carrera.duracion_segundos, 2),
                round(carrera.importe, 2)
            ])


        











######################################################################################################
###########TESTING####################################################################################
######################################################################################################



if __name__ == "__main__":

    historial = Historial("pruebas.csv")


    taxi = Taximetro()

    taxi.iniciar_carrera()
    carrera = Carrera("C001", "T001", taxi.inicio)

    time.sleep(0.1)
    taxi.cambiar_estado("movimiento")

    time.sleep(0.1)
    taxi.cambiar_estado("parado")

    time.sleep(0.1)

    importe_final = taxi.finalizar_carrera()
    carrera.finalizar(importe_final, taxi.fin_viaje)


    print("Cliente:", carrera.id_cliente)
    print("Taxista:", carrera.id_taxista)
    print("Duración:", round(carrera.duracion_segundos, 2), "segundos")
    print("Importe registrado:", f"{carrera.importe:.2f}", "€")


    historial.guardar(carrera)







