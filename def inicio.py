Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import hashlib

# Función para cifrar la contraseña utilizando SHA-256
def cifrar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Definimos la función para iniciar sesión
def inicio_sesion(usuario, contraseña):
    # Usuarios predefinidos
    usuarios_validos = {
        "admin": cifrar_contraseña("admin123"),
        "duran": cifrar_contraseña("duran456")
    }
    
    # Verificamos si el usuario existe y la contraseña es correcta
    if usuario in usuarios_validos:
        if usuarios_validos[usuario] == cifrar_contraseña(contraseña):
            return "¡Inicio de sesión exitoso!"
        else:
            return "Contraseña incorrecta."
    else:
        return "Usuario no encontrado."
))
