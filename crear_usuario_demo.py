
from autentificacion import Autenticacion

# Crear el gestor de autenticación
auth = Autenticacion()

# Credenciales exclusivas para demostración
usuario = "T001"
contrasena = "MiTaxi2026!!"

# Evitar registrar dos veces al mismo conductor
if usuario in auth.usuarios:
    print("El usuario de demostración ya existe.")
else:
    auth.registrar_usuario(usuario, contrasena)
    print("Usuario de demostración creado correctamente.")
