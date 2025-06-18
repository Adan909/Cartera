def actualizar_saldo(saldo_actual):
    """
    Permite al usuario ingresar una cantidad monetaria para actualizar el saldo disponible.

    Parámetros:
    saldo_actual (float): El saldo actual del usuario.

    Retorna:
    float: El nuevo saldo actualizado.
    """
    while True:
        try:
            cantidad = input("Ingresa la cantidad a agregar o restar (usa '-' para restar): $ ")
            cantidad = float(cantidad)

            saldo_actual += cantidad
            print(f"Saldo actualizado: ${saldo_actual:.2f}")
            return saldo_actual
        except ValueError:
            print("Por favor, ingresa un valor numérico válido.")

# Ejemplo de uso
saldo = 1000  # saldo inicial
saldo = actualizar_saldo(saldo)
