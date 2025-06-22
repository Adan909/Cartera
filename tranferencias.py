# Diccionario para almacenar saldos de los usuarios
saldos = {
    "admin": 1000.0,
    "duran": 750.0
}

# Función que muestra el saldo actual del usuario
def mostrar_saldo(usuario):
    saldo = saldos.get(usuario, 0.0)
    print(f"Saldo actual de {usuario}: ${saldo:.2f}")

# Función para realizar una transacción 
def transaccion(usuario):
    if usuario not in saldos:
        print("Este usuario no tiene una cuenta con saldo.")
        return
    
    while True:
        print("\n¿Deseas ingresar o retirar saldo?")
        opcion = input("Escribe 'ingresar', 'retirar' o 'salir': ").strip().lower()

        if opcion == "ingresar":
            cantidad = float(input("Cantidad a ingresar: "))
            saldos[usuario] += cantidad
            print(f"Ingreso exitoso. Nuevo saldo: ${saldos[usuario]:.2f}")
        
        elif opcion == "retirar":
            cantidad = float(input("Cantidad a retirar: "))
            if cantidad <= saldos[usuario]:
                saldos[usuario] -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: ${saldos[usuario]:.2f}")
            else:
                print("Fondos insuficientes.")
        
        elif opcion == "salir":
            break
        else:
            print("Opción no válida.")

