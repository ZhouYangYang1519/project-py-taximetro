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