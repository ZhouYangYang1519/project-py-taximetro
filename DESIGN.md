# Diseño del Taxímetro Digital

## 1. Objetivo

Diseñar un sistema de taxímetro en Python que permita gestionar carreras, controlar el estado del vehículo y calcular el importe según el tiempo transcurrido.

## 2. Estructura del programa

El programa está dividido en funciones con responsabilidades específicas:

| Función | Responsabilidad |
|---|---|
| `mostrar_instrucciones()` | Mostrar las instrucciones de uso |
| `arrancar()` | Iniciar una carrera |
| `leer_comando()` | Leer y validar los comandos |
| `is_moving()` | Comprobar el estado del vehículo |
| `cuenta_total()` | Calcular el importe acumulado |
| `gestionar_viaje()` | Gestionar una carrera completa |
| `main()` | Coordinar las carreras consecutivas |

## 3. Lógica de facturación

Se utilizan dos tarifas:

- Vehículo parado: 0,02 €/segundo.
- Vehículo en movimiento: 0,05 €/segundo.

El importe acumulado se calcula mediante:

**Importe nuevo = Importe anterior + Tarifa × Tiempo transcurrido**

## 4. Gestión de estados

El sistema distingue entre `parado` y `movimiento`.

Para evitar errores de facturación, primero se calcula el importe correspondiente al estado anterior y después se actualiza al nuevo estado.

## 5. Gestión de carreras

Cada carrera comienza con un importe de 0,00 €.

Al finalizar, se muestra el importe total y el conductor puede iniciar una nueva carrera sin reiniciar el programa.

## 6. Estado actual

Fase 1 implementada parcialmente. Pendiente de completar las pruebas de validación y la entrega final.

## 6. Estado actual del proyecto

Las fases 1, 2 y 3 se han implementado y se han validado sus funcionalidades principales.

- **Fase 1:** Implementación de la lógica básica de funcionamiento y facturación del taxímetro.
- **Fase 2:** Incorporación de configuración externa mediante JSON y registro de eventos mediante logging.
- **Fase 3:** Refactorización mediante programación orientada a objetos (POO), autenticación de conductores e interfaz gráfica con Tkinter.

Se han ejecutado satisfactoriamente 12 pruebas automatizadas y se ha verificado manualmente el funcionamiento de la interfaz gráfica.

## 7. Arquitectura orientada a objetos

La lógica principal del proyecto está implementada en `taximetro_oop.py`, mediante tres clases:

### 7.1. Clase Taximetro

Gestiona el funcionamiento y la facturación del taxímetro.

Responsabilidades principales:

- Iniciar y finalizar carreras.
- Gestionar los estados `parado` y `movimiento`.
- Calcular el importe según la tarifa y el tiempo transcurrido.
- Impedir operaciones inválidas, como iniciar dos carreras simultáneamente.
- Registrar eventos mediante logging.

### 7.2. Clase Carrera

Representa una carrera individual.

Almacena:

- Identificador del cliente.
- Identificador del conductor.
- Hora de inicio.
- Hora de finalización.
- Duración total.
- Importe final.

### 7.3. Clase Historial

Gestiona la persistencia de las carreras finalizadas mediante un archivo CSV.

Los datos almacenados incluyen fecha, cliente, conductor, duración e importe.

## 8. Sistema de autenticación

El archivo `autentificacion.py` contiene la clase `Autenticacion`.

El sistema permite registrar conductores y verificar sus credenciales.

Las contraseñas no se almacenan en texto plano. Se utiliza PBKDF2-HMAC-SHA256 con una sal aleatoria para generar un hash de cada contraseña.

Los datos se guardan localmente en `usuarios.json`, excluido del repositorio mediante `.gitignore`.

La autenticación se integra tanto en la interfaz de línea de comandos como en la interfaz gráfica.

## 9. Interfaz gráfica de usuario

La interfaz se implementa mediante Tkinter en `taximetro_GUI.py`.

Permite realizar las siguientes operaciones:

- Iniciar sesión como conductor.
- Introducir el identificador del cliente.
- Iniciar una carrera.
- Cambiar entre los estados `parado` y `movimiento`.
- Consultar el importe acumulado en tiempo real.
- Finalizar una carrera.
- Guardar automáticamente la información en el historial CSV.

### Actualización del importe

Se utiliza el método `after()` de Tkinter para actualizar periódicamente el importe mostrado.

El importe visual se calcula a partir de la cantidad acumulada, la tarifa del estado actual y el tiempo transcurrido.

Esta actualización no modifica directamente la cuenta real del taxímetro, evitando una doble facturación.

## 10. Organización del proyecto

| Archivo | Responsabilidad |
|---|---|
| `taximeter.py` | Implementación procedural inicial |
| `config.json` | Configuración de tarifas |
| `taximetro_oop.py` | Lógica orientada a objetos |
| `autentificacion.py` | Registro y autenticación de usuarios |
| `app.py` | Interfaz de línea de comandos (CLI) |
| `taximetro_GUI.py` | Interfaz gráfica (GUI) |
| `historial.csv` | Historial de carreras |
| `test_taximetro_oop.py` | Pruebas de la lógica orientada a objetos |
| `test_autentificacion.py` | Pruebas del sistema de autenticación |

## 11. Validación y pruebas

Se han realizado pruebas automatizadas mediante `unittest` para validar la lógica de facturación y el sistema de autenticación.

Resultado de la última ejecución:

- **12 pruebas ejecutadas.**
- **12 pruebas superadas.**
- **0 errores y 0 fallos.**

Además, se ha probado manualmente el flujo completo de la interfaz gráfica:

**Login → Identificación del cliente → Inicio de carrera → Cambio de estado → Finalización → Registro CSV.**

La documentación de las pruebas se encuentra en `TESTING.md`.

