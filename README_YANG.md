# 🚕 Taxímetro Digital — Implementación de Yang

## 1. Descripción del proyecto

Este proyecto consiste en desarrollar un taxímetro digital utilizando Python, capaz de calcular el importe de una carrera según el tiempo transcurrido y el estado del vehículo.

El proyecto se ha desarrollado de forma progresiva, incorporando programación orientada a objetos, configuración externa, registro de eventos, autenticación de usuarios e interfaz gráfica.

## 2. Tecnologías utilizadas

- Python 3
- Tkinter — Interfaz gráfica de usuario (GUI)
- JSON — Configuración y almacenamiento de usuarios
- CSV — Historial de carreras
- Logging — Registro de eventos
- Unittest — Pruebas automatizadas
- Hashlib y Secrets — Protección de contraseñas

## 3. Fases del proyecto

### FASE 1 — Funcionalidad básica

Implementación inicial del taxímetro mediante programación procedural.

- Inicio y finalización de carreras.
- Estados de movimiento y parada.
- Cálculo del importe según el tiempo transcurrido.
- Registro del historial en formato CSV.

Archivo principal: `taximeter.py`

### FASE 2 — Configuración y logging

- Configuración de tarifas mediante `config.json`.
- Registro de eventos mediante logging.
- Gestión de mensajes informativos y errores.

Archivo de registro: `taximetro.log`

### FASE 3 — Programación orientada a objetos y GUI

Se han desarrollado tres clases principales:

- `Taximetro`: gestiona los estados del vehículo y el cálculo del importe.
- `Carrera`: almacena la información de una carrera.
- `Historial`: guarda los registros de las carreras en CSV.

También se ha incorporado:

- Autenticación de conductores con contraseñas protegidas mediante PBKDF2.
- Interfaz gráfica desarrollada con Tkinter.
- Visualización del importe en tiempo real.
- Registro de identificadores de conductor y cliente.
- Almacenamiento automático de carreras finalizadas.

Archivos principales:

- `taximetro_oop.py`
- `autentificacion.py`
- `taximetro_GUI.py`
- `app.py`

## 4. Cómo ejecutar el proyecto

### Requisitos

Tener instalado Python 3 con soporte para Tkinter.

El programa utiliza bibliotecas de la biblioteca estándar de Python, por lo que no necesita dependencias externas adicionales.

### Ejecutar la interfaz gráfica

Abrir una terminal en la carpeta raíz del proyecto y ejecutar:

```bash
python taximetro_GUI.py
```

Si el comando `python` no está disponible, utilizar la ruta del intérprete de Python instalado.

### Autenticación

Para utilizar el taxímetro es necesario iniciar sesión con un conductor registrado.

Las credenciales se almacenan localmente en `usuarios.json`, archivo excluido del repositorio mediante `.gitignore`.

**Usuario de demostración previsto:**

- Usuario: `T001`
- Contraseña: `MiTaxi2026!!`

El usuario de demostración debe registrarse previamente. Se incluirá un procedimiento de inicialización para facilitar las pruebas.

## 5. Funcionamiento de la interfaz gráfica

1. Pulsar **Login** e introducir las credenciales.
2. Pulsar **Iniciar carrera**.
3. Introducir el identificador del cliente.
4. Seleccionar **Movimiento** o **Parado** según el estado del vehículo.
5. Consultar el importe acumulado, actualizado automáticamente.
6. Pulsar **Finalizar carrera**.
7. Consultar el importe final y el registro guardado en `historial.csv`.

## 6. Pruebas

El proyecto incluye pruebas automatizadas para la lógica del taxímetro y la autenticación.

Para ejecutarlas:

```bash
python -m unittest discover -v
```

**Última ejecución verificada:**

- 12 pruebas automatizadas.
- 12 pruebas superadas.
- Resultado: `OK`.

También se ha comprobado manualmente el funcionamiento de la interfaz gráfica y el almacenamiento de carreras en CSV.

## 7. Archivos de documentación

- `README.md`: enunciado original del proyecto.
- `README_YANG.md`: documentación de esta implementación.
- `DESIGN.md`: documentación técnica del diseño.
- `TESTING.md`: documentación de pruebas.

## 8. Autora

Yang Yang

Proyecto desarrollado durante el bootcamp de Inteligencia Artificial de Factoría F5, Madrid.