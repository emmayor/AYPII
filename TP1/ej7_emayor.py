# Una de las técnicas de criptografía más rudimentarias consiste en sustituir cada uno de los caracteres del alfabeto
# por otro situado n posiciones más a la derecha. Si n = 2, por ejemplo, sustituiremos la a por la c, la b por la d, y así
# sucesivamente. El problema que aparece en las últimas n letras del alfabeto tiene fácil solución: en el ejemplo, la
# letra y se sustituirá por la a y la letra z por la b. La sustitución debe aplicarse a las letras minúsculas y mayúsculas
# y a los dígitos. Diseñar un programa que lea un texto y el valor de n y muestre su versión criptográfica.

# (<caracter-a-codificar> + <valor-clave> - <inicio-de-caracteres>) % <cantidad-de-caracteres> + <inicio-de-caracteres>
# Al caracter original se le suma el valor de la llave "z" y luego se le resta el código del primer caracter
# de su secuencia (la sucesión de letras o números en la tabla ASCII; el primer elemento
# tiene representación decimal 48 para digitos, 65 para letras mayúsculas y 97 para minúsculas)
# El resultado es la "distancia" del caracter en cuestion respecto del primero.
# Se divide esto entre la cantidad de caracteres de la secuencia (26 para letras, 10 para números), 
# ya que si la cuenta anterior es mayor a 26 (o a 10), el caracter resultante estaría fuera de rango
# El resto de esta division, más el valor del primer caracter, nos devuelve el caracter codificado. 

def encriptar(cadena,clave):
    long = len(cadena)
    cadenaSalida = ""
    cadena_list = list(cadena)
    for i in cadena_list:
        char_code = ord(i)
        # SI ES UN NÚMERO...
        if char_code in range(48,58):
            cadenaSalida += chr((char_code + clave - 48) % 10 + 48)
        # SI ES MAYÚSCULA...
        elif i.isupper():
            cadenaSalida += chr((char_code + clave - 65) % 26 + 65)
        # SI ES UN ESPACIO
        elif char_code == 32:
            cadenaSalida += " "
        # SI ES MINÚSCULA...
        else:
            cadenaSalida += chr((char_code + clave - 97) % 26 + 97)
    return cadenaSalida

texto = input("Ingrese una frase\n> ")
clave = int(input("Ingrese un número para codificar la frase\n> "))
resultado = encriptar(texto,clave)
print(f"Texto encriptado: {resultado}")



