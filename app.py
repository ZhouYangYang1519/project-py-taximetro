
# Importar los módulos de autenticación y del taxímetro
from autentificacion import Autenticacion
from taximetro_oop import Taximetro, Carrera, Historial


from getpass import getpass  # Ocultar la contraseña al escribirla



def main():
    # Crear los objetos necesarios para ejecutar la aplicación
    auth = Autenticacion()
    taxi = Taximetro()

    # Solicitar las credenciales del conductor
    usuario = input("Introduce tu usuario: ")
    contrasena = getpass("Introduce tu contraseña: ")

    # Verificar la identidad antes de permitir el acceso
    if not auth.autentificar_usuario(usuario, contrasena):
        print("Acceso denegado")
        return


    print("Acceso autorizado")
    print("Bienvenido,", usuario)

    # Iniciar una carrera después de autenticar al conductor
    taxi.iniciar_carrera()


    # Solicitar el identificador del cliente
    # Solicitar un ID de cliente obligatorio
    id_cliente = input("Introduce el ID del cliente: ").strip()

    while not id_cliente:
        print("El ID del cliente no puede estar vacío")
        id_cliente = input("Introduce el ID del cliente: ").strip()

    # Crear la carrera con el conductor autenticado
    carrera = Carrera(id_cliente, usuario, taxi.inicio)
    
    
    
    
    historial = Historial("pruebas.csv")











    # Mostrar el estado inicial del taxímetro
    print("Estado inicial:", taxi.estado)
    print("Cuenta inicial:", f"{taxi.cuenta:.2f}", "€")

    
    # Permitir varios cambios de estado durante la carrera
    while taxi.viaje_activo:
        comando = input(
            "Introduce parado, movimiento o T para terminar: "
        ).strip().lower()

        # Finalizar la carrera cuando el conductor introduce T
        if comando == "t":
            # Finalizar la carrera y recuperar el importe
            importe_final = taxi.finalizar_carrera()

            # Registrar el importe y la duración de la carrera
            carrera.finalizar(importe_final, taxi.fin_viaje)

            # Guardar la carrera en el archivo CSV
            historial.guardar(carrera)

            print("Carrera guardada correctamente")
            break



        # Actualizar el estado y calcular el importe acumulado
        try:
            taxi.cambiar_estado(comando)
        except ValueError as error:
            print("Error:", error)




if __name__ == "__main__":
    main()
