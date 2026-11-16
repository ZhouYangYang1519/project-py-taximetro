from taximeter import cuenta_total, is_moving


assert cuenta_total(0, "movimiento", 10) == 0.50
print("TEST movimiento: OK")

assert cuenta_total(0, "parado", 10) == 0.20
print("TEST parado: OK")

try:
    is_moving("volar")
except ValueError:
    print("TEST estado inválido: OK")
else:
    raise AssertionError("Debería lanzar ValueError")
