# un diccionario que almacena el saldo de los usuarios
saldos_usuarios = {}

# muestra el saldo de un usuario si no existe se solicitara el saldo al usuario
def ver_saldo(usuario):
    if usuario in saldos_usuarios:
        return f"El saldo de '{usuario}' es: C${saldos_usuarios[usuario]:.2f}"
    else:
        try:
            saldo_inicial = float(input(f"No se encontró saldo para '{usuario}'. Ingrese el saldo inicial: C$ "))
            saldos_usuarios[usuario] = saldo_inicial
            return f"Saldo registrado. El saldo de '{usuario}' es: C${saldo_inicial:.2f}"
        except ValueError:
            return "Error: Ingrese un numero válido para el saldo."
