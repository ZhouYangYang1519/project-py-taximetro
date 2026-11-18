
import hashlib  # Biblioteca para generar hashes de contraseñas
import secrets  # Biblioteca para generar valores aleatorios seguros
import json  # Biblioteca para leer y escribir archivos JSON
from pathlib import Path  # Herramienta para gestionar rutas de archivos


class Autenticacion:

    def __init__(self, archivo="usuarios.json"):
        # Definir la ruta del archivo donde se guardarán los usuarios
        self.archivo = Path(archivo)

        # Comprobar si el archivo de usuarios ya existe
        if self.archivo.exists():

            # Abrir el archivo y cargar los usuarios registrados
            with open(self.archivo, "r", encoding="utf-8") as fichero:
                self.usuarios = json.load(fichero)

        else:
            # Si el archivo no existe, crear un diccionario vacío
            self.usuarios = {}

    def registrar_usuario(self, nombre_usuario, contrasena):
        # Comprobar si el nombre de usuario ya está registrado
        if nombre_usuario in self.usuarios:
            raise ValueError("El usuario ya existe")

        # Generar un salt aleatorio y diferente para cada usuario
        salt = secrets.token_bytes(16)

        # Generar un hash seguro utilizando PBKDF2 y SHA-256
        # Las iteraciones dificultan los ataques de fuerza bruta
        hash_contrasena = hashlib.pbkdf2_hmac(
            "sha256",
            contrasena.encode("utf-8"),
            salt,
            600_000
        )

        # Guardar el salt y el hash, sin almacenar la contraseña original
        # Cada usuario tiene sus propios datos de autenticación
        self.usuarios[nombre_usuario] = {
            "salt": salt.hex(),
            "hash": hash_contrasena.hex()
        }
        # Guardar los cambios después del registro
        self.guardar_usuarios()






    def guardar_usuarios(self):
        # Guardar los usuarios registrados en un archivo JSON
        with open(self.archivo, "w", encoding="utf-8") as fichero:
            json.dump(self.usuarios, fichero, indent=4)











    def autentificar_usuario(self, nombre_usuario, contrasena):
        # Comprobar si el usuario está registrado
        if nombre_usuario not in self.usuarios:
            return False

        # Recuperar los datos del usuario desde el diccionario
        datos = self.usuarios[nombre_usuario]

   
        # Recuperar los datos binarios desde sus valores hexadecimales
        salt = bytes.fromhex(datos["salt"])
        hash_guardado = bytes.fromhex(datos["hash"])

        # Calcular un nuevo hash utilizando la contraseña introducida
        # Es necesario utilizar el mismo salt y número de iteraciones
        hash_intento = hashlib.pbkdf2_hmac(
            "sha256",
            contrasena.encode("utf-8"),
            salt,
            600_000
        )

        # Comparar ambos hashes de forma segura
        # Devuelve True si coinciden y False si son diferentes
        return secrets.compare_digest(hash_intento, hash_guardado)


# Ejecutar las pruebas manuales solamente al iniciar este archivo
if __name__ == "__main__":

    # Crear el gestor de autenticación
    auth = Autenticacion()

    # Registrar un usuario de prueba
    # Registrar el usuario solo si todavía no existe
    if "T001" not in auth.usuarios:
        auth.registrar_usuario("T001", "MiTaxi2026!")

    # Verificar que la contraseña correcta permite autenticarse
    print("Contraseña correcta:",
          auth.autentificar_usuario("T001", "MiTaxi2026!"))

    # Verificar que una contraseña incorrecta es rechazada
    print("Contraseña incorrecta:",
          auth.autentificar_usuario("T001", "incorrecta"))

    # Verificar que un usuario inexistente no puede autenticarse
    print("Usuario inexistente:",
          auth.autentificar_usuario("T999", "MiTaxi2026!"))





