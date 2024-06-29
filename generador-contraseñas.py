import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_deseada = 7  
nueva_contrasena = generar_contrasena(longitud_deseada)
print("Contraseña generada:", nueva_contrasena)