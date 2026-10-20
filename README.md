Simulación de una tiendita

Proyecto de simulación hecho en Python. Se ejecuta en la terminal (sin interfaz gráfica).

¿De qué trata?

Simula las ventas de una tiendita. Los clientes van llegando poco a poco y cada uno compra un producto (refresco, papitas o torta). Al final el programa nos dice cuánto se vendió y cuánto dinero se ganó.

Distribuciones y métodos que usamos
Qué simulamos	Distribución	Método
Cada cuánto llega un cliente	Exponencial	Transformada inversa
Qué producto compra el cliente	Discreta (con porcentajes)	Transformada inversa discreta
Fórmulas

Exponencial:

x = -media * ln(1 - U)

donde U es un número aleatorio entre 0 y 1.

Discreta: se genera un número aleatorio y se compara con los porcentajes acumulados. Por ejemplo, con 50% / 30% / 20%:

de 0 a 50 -> Refresco
de 50 a 80 -> Papitas
de 80 a 100 -> Torta
Cómo se ejecuta
Tener Python 3 instalado.
Abrir la terminal en la carpeta del proyecto.
Correr:
python simulacion_tienda.py
Datos que pide el programa
Cuántos clientes quieres simular.
Cada cuántos minutos llega un cliente (en promedio).
El porcentaje de clientes que compra cada producto (tiene que sumar 100).
Ejemplo

Entrada:

Clientes a simular: 50
Minutos entre llegadas: 3
Refresco (%): 50
Papitas (%): 30
Torta (%): 20

Salida (puede cambiar, porque es aleatoria):

=== RESULTADOS ===
Tiempo total simulado: 133.7 minutos (2.23 horas)
Refresco: 24 vendidos ($480)
Papitas: 11 vendidos ($165)
Torta: 15 vendidos ($600)
Ingreso total: $1245
Precios usados
Producto	Precio
Refresco	$20
Papitas	$15
Torta	$40
