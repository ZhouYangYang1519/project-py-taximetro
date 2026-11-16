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