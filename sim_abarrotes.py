"""
Simulación sencilla: ventas en una tiendita

Distribución y método:
1) Exponencial (tiempo entre llegadas de clientes) -> transformada inversa
       x = -media * ln(1 - U)
2) Discreta (qué producto compra cada cliente) -> transformada inversa discreta
       se compara U contra los porcentajes acumulados
"""

import math
import random

PRODUCTOS = ["Refresco", "Papitas", "Torta"]
PRECIOS = [20, 15, 40]


def exponencial(media):
    u = random.random()
    return -media * math.log(1 - u)


def elegir_producto(porcentajes):
    u = random.random() * 100
    acumulado = 0
    for i, p in enumerate(porcentajes):
        acumulado += p
        if u < acumulado:
            return i
    return len(porcentajes) - 1


# ---------- Entrada de datos ----------
print("=== SIMULACIÓN DE UNA TIENDITA ===")
clientes = int(input("¿Cuántos clientes quieres simular? "))
media = float(input("Cada cuántos minutos llega un cliente (promedio)? "))

print("Porcentaje de clientes que compra cada producto (debe sumar 100):")
porcentajes = []
for nombre in PRODUCTOS:
    porcentajes.append(float(input(f"  {nombre} (%): ")))

if sum(porcentajes) != 100:
    print("Los porcentajes no suman 100. Ejecuta de nuevo.")
    raise SystemExit

# ---------- Simulación ----------
reloj = 0
ventas = [0] * len(PRODUCTOS)
dinero = 0

for _ in range(clientes):
    reloj += exponencial(media)
    i = elegir_producto(porcentajes)
    ventas[i] += 1
    dinero += PRECIOS[i]

# ---------- Salida ----------
print("\n=== RESULTADOS ===")
print(f"Tiempo total simulado: {reloj:.1f} minutos ({reloj / 60:.2f} horas)")
for nombre, cantidad, precio in zip(PRODUCTOS, ventas, PRECIOS):
    print(f"{nombre}: {cantidad} vendidos (${cantidad * precio})")
print(f"Ingreso total: ${dinero}")