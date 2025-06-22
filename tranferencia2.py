# Diccionario para almacenar los saldos de los usuarios
saldos = {
    "admin": 1000.0,
    "duran": 750.0
}

# Función para realizar transacciones 
def transaccion(usuario, tipo, monto):
    if usuario not in saldos:
        return "Usuario no tiene cuenta asociada."
    
    if tipo == "ingresar":
        saldos[usuario] += monto
        return f"Has ingresado ${monto:.2f}. Nuevo saldo: ${saldos[usuario]:.2f}"
    
    elif tipo == "retirar":
        if monto > saldos[usuario]:
            return "Fondos insuficientes."
        saldos[usuario] -= monto
        return f"Has retirado ${monto:.2f}. Nuevo saldo: ${saldos[usuario]:.2f}"
    
    else:
        return "Tipo de transacción no válido. Usa 'ingresar' o 'retirar'."
