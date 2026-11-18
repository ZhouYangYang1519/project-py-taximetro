# Pruebas de funcionamiento — Fase 1

## Objetivo

Verificar el funcionamiento del MVP del taxímetro desarrollado en Python.

## Pruebas manuales

| Prueba | Procedimiento | Resultado observado | Estado |
|---|---|---|---|
| Entrada inválida | Introducir `hello` como comando | El programa muestra `Comando no válido` y solicita otro comando | Superada |
| Cambio de estado | Cambiar de `parado` a `movimiento` | El programa actualiza el estado y acumula el importe | Superada |
| Finalización de carrera | Introducir `t` | Se muestra el importe final con dos decimales | Superada |
| Carreras consecutivas | Finalizar una carrera, introducir `S` e iniciar otra con un nuevo cliente | Se inicia una nueva carrera sin reiniciar el programa | Superada |
| Cierre del programa | Introducir `N` después de una carrera | Se muestra `Taxímetro cerrado` y se vuelve a la terminal | Superada |

## Observaciones

- Las tarifas utilizadas son 0,02 €/segundo en estado `parado` y 0,05 €/segundo en estado `movimiento`.
- Se ha comprobado manualmente la acumulación de importes al cambiar de estado.
- La precisión del cálculo temporal todavía no se ha verificado mediante pruebas automatizadas con tiempos controlados.
- El importe se actualiza visualmente al introducir un comando, no de forma continua en pantalla.

## Conclusión

Las pruebas manuales realizadas no han mostrado errores en los flujos principales de la Fase 1. Queda pendiente la validación automatizada de los cálculos.



## FASE 2 — Pruebas realizadas

- **Logging:** registro de inicio y fin de viaje, importe final y comandos inválidos.
- **Persistencia:** almacenamiento de fecha, cliente, taxista, duración e importe en `historial.csv`. Verificada la adición de nuevas carreras sin sobrescribir las anteriores.
- **Configuración:** lectura de tarifas desde `config.json`. Verificado el cambio de tarifa de parado de 0.02 a 0.10 €/segundo y su restauración.
- **Testing automático:** pruebas de `movimiento`, `parado` y estado inválido con `assert` y `ValueError`.

**Resultado:** las pruebas realizadas finalizaron correctamente.

## Pruebas de la Fase 3 — POO, autenticación y GUI

### 1. Pruebas automatizadas

Se utiliza la biblioteca estándar `unittest` para comprobar el funcionamiento de la lógica orientada a objetos y del sistema de autenticación.

Para ejecutar todas las pruebas:

```bash
python -m unittest discover -v
```

**Resultado obtenido el 18/11/2026:**

- Pruebas ejecutadas: 12
- Pruebas superadas: 12
- Errores: 0
- Fallos: 0
- Resultado: `OK`

### 2. Pruebas del taxímetro orientado a objetos

Archivo: `test_taximetro_oop.py`

Se han verificado:

- Estado inicial del taxímetro.
- Inicio y finalización de carreras.
- Cálculo del importe.
- Validación de estados incorrectos.
- Prevención de carreras duplicadas.
- Prevención de finalizaciones sin carrera activa.

**Resultado: 6/6 pruebas superadas.**

### 3. Pruebas de autenticación

Archivo: `test_autentificacion.py`

Se han verificado:

- Registro de un nuevo usuario.
- Detección de usuarios duplicados.
- Autenticación con contraseña correcta.
- Rechazo de contraseñas incorrectas.
- Rechazo de usuarios inexistentes.
- Persistencia de los datos en JSON.

**Resultado: 6/6 pruebas superadas.**

### 4. Pruebas manuales de la interfaz gráfica

Archivo: `taximetro_GUI.py`

| Prueba | Resultado |
|---|---|
| Inicio de sesión con credenciales válidas | OK |
| Desbloqueo del botón de inicio tras autenticación | OK |
| Introducción del ID del cliente | OK |
| Inicio de carrera | OK |
| Cambio entre movimiento y parada | OK |
| Actualización automática del importe | OK |
| Finalización de carrera | OK |
| Bloqueo de botones tras finalizar | OK |
| Registro de carrera en CSV | OK |

### 5. Verificación del historial

Se ha comprobado que las carreras finalizadas se añaden al archivo `historial.csv`.

Ejemplos de registros obtenidos:

| Cliente | Conductor | Duración (s) | Importe (€) |
|---|---|---:|---:|
| C002 | T001 | 11.00 | 0.34 |
| C002 | T001 | 3.22 | 0.11 |

El archivo conserva los registros anteriores al añadir nuevas carreras.

### 6. Conclusión

Las funcionalidades principales de las fases 1, 2 y 3 se han implementado y se han validado mediante pruebas automatizadas y pruebas manuales.

Las pruebas realizadas confirman el funcionamiento básico del cálculo de tarifas, la autenticación y el registro de carreras.

La interfaz gráfica ha sido verificada manualmente; no se dispone de una suite de pruebas automáticas específica para Tkinter.
