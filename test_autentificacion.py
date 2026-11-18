
import unittest
import tempfile
from pathlib import Path

from autentificacion import Autenticacion


class TestAutenticacion(unittest.TestCase):

    def setUp(self):
        # Crear un directorio temporal para las pruebas
        self.directorio = tempfile.TemporaryDirectory()
        self.archivo = Path(self.directorio.name) / "usuarios_test.json"

        # Crear un gestor de autenticación independiente
        self.auth = Autenticacion(self.archivo)

    def tearDown(self):
        # Eliminar los archivos temporales después de cada prueba
        self.directorio.cleanup()

    def test_registrar_usuario(self):
        # Comprobar que el usuario se registra correctamente
        self.auth.registrar_usuario("T001", "ClavePrueba123!")

        self.assertIn("T001", self.auth.usuarios)
        self.assertIn("salt", self.auth.usuarios["T001"])
        self.assertIn("hash", self.auth.usuarios["T001"])

    def test_contrasena_correcta(self):
        # Verificar el acceso con la contraseña correcta
        self.auth.registrar_usuario("T001", "ClavePrueba123!")

        resultado = self.auth.autentificar_usuario(
            "T001", "ClavePrueba123!"
        )
        self.assertTrue(resultado)

    def test_contrasena_incorrecta(self):
        # Rechazar una contraseña incorrecta
        self.auth.registrar_usuario("T001", "ClavePrueba123!")

        resultado = self.auth.autentificar_usuario(
            "T001", "incorrecta"
        )
        self.assertFalse(resultado)

    def test_usuario_inexistente(self):
        # Rechazar usuarios que no están registrados
        resultado = self.auth.autentificar_usuario(
            "T999", "ClavePrueba123!"
        )
        self.assertFalse(resultado)

    def test_usuario_duplicado(self):
        # Impedir que se registre dos veces el mismo usuario
        self.auth.registrar_usuario("T001", "ClavePrueba123!")

        with self.assertRaises(ValueError):
            self.auth.registrar_usuario("T001", "OtraClave123!")

    def test_persistencia_json(self):
        # Registrar un usuario y guardarlo en JSON
        self.auth.registrar_usuario("T001", "ClavePrueba123!")

        # Crear otro objeto para comprobar la lectura del archivo
        nueva_auth = Autenticacion(self.archivo)

        self.assertTrue(
            nueva_auth.autentificar_usuario("T001", "ClavePrueba123!")
        )


if __name__ == "__main__":
    unittest.main()




