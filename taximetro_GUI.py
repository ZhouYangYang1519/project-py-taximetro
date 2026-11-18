
import tkinter as tk  # Biblioteca para crear interfaces gráficas
from taximetro_oop import Taximetro, Carrera, Historial
import time  # Biblioteca para calcular el tiempo transcurrido
from tkinter import simpledialog, messagebox
from autentificacion import Autenticacion





# Crear el objeto que gestiona el cálculo del importe
taxi = Taximetro()

# Crear el gestor del historial de carreras
historial = Historial("historial.csv")

# Guardar los datos de la carrera actual
carrera_actual = None

# Crear el gestor de autenticación
auth = Autenticacion()

# Guardar el conductor que ha iniciado sesión
usuario_actual = None





# Crear la ventana principal
ventana = tk.Tk()

# Configurar el título y el tamaño de la ventana
ventana.title("Taxímetro Digital")
ventana.geometry("450x500")

# Mostrar un mensaje de bienvenida
etiqueta = tk.Label(
    ventana,
    text="Bienvenido al Taxímetro Digital",
    font=("Arial", 16)
)

# Colocar el texto dentro de la ventana
etiqueta.pack(pady=30)




# Autenticar al conductor antes de utilizar el taxímetro
def iniciar_sesion():
    global usuario_actual

    # Solicitar las credenciales del conductor
    usuario = simpledialog.askstring(
        "Login", "Introduce tu usuario:", parent=ventana
    )

    if usuario is None:
        return

    contrasena = simpledialog.askstring(
        "Login", "Introduce tu contraseña:",
        show="*", parent=ventana
    )

    if contrasena is None:
        return

    # Verificar el usuario y la contraseña
    if auth.autentificar_usuario(usuario, contrasena):
        usuario_actual = usuario
        messagebox.showinfo("Login", "Acceso autorizado")

        # Permitir iniciar una carrera
        boton.config(state="normal")
        boton_login.config(state="disabled")
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos")












# Iniciar una carrera después de identificar al cliente
def iniciar():
    global carrera_actual

    if usuario_actual is None or taxi.viaje_activo:
        return

    # Solicitar el identificador del cliente
    id_cliente = simpledialog.askstring(
        "Cliente",
        "Introduce el ID del cliente:",
        parent=ventana
    )

    # No iniciar la carrera si se cancela o se deja vacío
    if id_cliente is None or not id_cliente.strip():
        messagebox.showwarning(
            "Cliente",
            "Debes introducir un ID de cliente válido"
        )
        return

    # Iniciar el taxímetro y crear la carrera asociada
    taxi.iniciar_carrera()
    carrera_actual = Carrera(
        id_cliente.strip(),
        usuario_actual,
        taxi.inicio
    )

    # Actualizar la interfaz
    etiqueta_estado.config(text="Estado: parado")
    etiqueta_cuenta.config(text="Importe: 0.00 €")

    boton.config(state="disabled")
    boton_movimiento.config(state="normal")
    boton_parado.config(state="normal")
    boton_finalizar.config(state="normal")







# Crear un botón de prueba
boton = tk.Button(
    ventana,
    text="Iniciar carrera",
    font=("Arial", 12),
    command=iniciar
)


# Mostrar el estado actual del taxímetro
etiqueta_estado = tk.Label(
    ventana,
    text="Estado: sin carrera",
    font=("Arial", 12)
)
etiqueta_estado.pack(pady=10)

# Mostrar el importe acumulado de la carrera
etiqueta_cuenta = tk.Label(
    ventana,
    text="Importe: 0.00 €",
    font=("Arial", 16)
)
etiqueta_cuenta.pack(pady=10)



# Colocar el botón en la ventana
boton.pack(pady=10)


# Cambiar el estado del taxímetro a movimiento
def movimiento():
    taxi.cambiar_estado("movimiento")
    etiqueta_estado.config(text="Estado: movimiento")
    # Actualizar el importe mostrado en la interfaz
    etiqueta_cuenta.config(text=f"Importe: {taxi.cuenta:.2f} €")


# Cambiar el estado del taxímetro a parado
def parado():
    taxi.cambiar_estado("parado")
    etiqueta_estado.config(text="Estado: parado")
    # Actualizar el importe mostrado en la interfaz
    etiqueta_cuenta.config(text=f"Importe: {taxi.cuenta:.2f} €")    




# Finalizar la carrera y guardar los datos en el historial
def finalizar():
    global carrera_actual

    if not taxi.viaje_activo:
        return

    # Calcular el importe definitivo
    importe_final = taxi.finalizar_carrera()

    # Completar la carrera con el importe y la hora de finalización
    carrera_actual.finalizar(importe_final, taxi.fin_viaje)

    # Guardar los datos en el archivo CSV
    historial.guardar(carrera_actual)

    # Actualizar la interfaz
    etiqueta_estado.config(text="Estado: finalizado")
    etiqueta_cuenta.config(
        text=f"Importe final: {importe_final:.2f} €"
    )

    # Preparar la interfaz para una nueva carrera
    boton.config(state="normal")
    boton_movimiento.config(state="disabled")
    boton_parado.config(state="disabled")
    boton_finalizar.config(state="disabled")

    carrera_actual = None

    messagebox.showinfo(
        "Carrera finalizada",
        "La carrera se ha guardado correctamente en el historial."
    )





# Actualizar el importe mostrado sin modificar la cuenta real
def actualizar_importe():
    if taxi.viaje_activo:
        # Calcular el tiempo transcurrido desde el último cambio de estado
        tiempo = time.time() - taxi.inicio

        # Consultar la tarifa correspondiente al estado actual
        if taxi.is_moving():
            tarifa = taxi.config["tarifa_movimiento"]
        else:
            tarifa = taxi.config["tarifa_parado"]

        # Calcular el importe provisional para mostrarlo en pantalla
        importe_visual = taxi.cuenta + tarifa * tiempo

        # Actualizar únicamente la etiqueta de la interfaz
        etiqueta_cuenta.config(
            text=f"Importe: {importe_visual:.2f} €"
        )

    # Programar la siguiente actualización dentro de 500 ms
    ventana.after(500, actualizar_importe)









# Crear botones para cambiar el estado
boton_movimiento = tk.Button(
    ventana,
    text="Movimiento",
    font=("Arial", 12),
    command=movimiento
)
boton_movimiento.pack(pady=5)

boton_parado = tk.Button(
    ventana,
    text="Parado",
    font=("Arial", 12),
    command=parado
)
boton_parado.pack(pady=5)




# Crear el botón para finalizar la carrera
boton_finalizar = tk.Button(
    ventana,
    text="Finalizar carrera",
    font=("Arial", 12),
    command=finalizar
)
boton_finalizar.pack(pady=5)



# Desactivar los controles hasta iniciar una carrera
boton_movimiento.config(state="disabled")
boton_parado.config(state="disabled")
boton_finalizar.config(state="disabled")
# Bloquear el inicio de carreras hasta iniciar sesión
boton.config(state="disabled")


# Iniciar la actualización periódica de la interfaz
ventana.after(500, actualizar_importe)


# Crear el botón para iniciar sesión
boton_login = tk.Button(
    ventana,
    text="Login",
    font=("Arial", 12),
    command=iniciar_sesion
)
boton_login.pack(pady=5)




# Mantener la ventana abierta y esperar eventos
ventana.mainloop()
