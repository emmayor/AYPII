# La función para desencriptar es similar a la de encriptar. En lugar de 
# añadir la clave se sustrae...

def desencriptar(cadena,clave):
    long = len(cadena)
    cadenaSalida = ""
    for i in range(long):
        char = cadena[i]
        char_code = ord(char)
        # SI ES UN NÚMERO...
        if char_code in range(48,58):
            cadenaSalida += chr((char_code - clave - 48) % 10 + 48)
        # SI ES MAYÚSCULA...
        elif char.isupper():
            cadenaSalida += chr((char_code - clave - 65) % 26 + 65)
        # SI ES UN ESPACIO
        elif char_code == 32:
            cadenaSalida += " "
        # SI ES MINÚSCULA...
        else:
            cadenaSalida += chr((char_code - clave - 97) % 26 + 97)
    return cadenaSalida

texto = input("Ingrese una frase codificada\n> ")
clave = int(input("Ingrese la clave para decodificar la frase\n> "))
resultado = desencriptar(texto,clave)
print(f"Texto desencriptado: {resultado}")