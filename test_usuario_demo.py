
import os
import tempfile
from autentificacion import Autenticacion

# Simular un entorno limpio sin usuarios registrados
with tempfile.TemporaryDirectory() as carpeta:
    archivo = os.path.join(carpeta, "usuarios_demo.json")

    # Crear un gestor con un archivo JSON nuevo
    auth = Autenticacion(archivo)

    usuario = "T001"
    contrasena = "MiTaxi2026!!"

    # Registrar el conductor de demostración
    auth.registrar_usuario(usuario, contrasena)

    # Simular un nuevo inicio del programa
    nueva_sesion = Autenticacion(archivo)

    # Verificar que el conductor puede iniciar sesión
    assert nueva_sesion.autentificar_usuario(usuario, contrasena)

    # Verificar que una contraseña incorrecta es rechazada
    assert not nueva_sesion.autentificar_usuario(usuario, "incorrecta")

    print("OK: registro y autenticación del usuario demo.")
    print("OK: persistencia de credenciales en JSON.")
    print("OK: contraseña incorrecta rechazada.")


