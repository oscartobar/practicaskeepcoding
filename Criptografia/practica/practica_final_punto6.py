#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 6

from Crypto.Hash import HMAC, SHA256
from base64 import b64decode, b64encode
import jks
import os

try:

    # Obteniendo el path
    path = os.path.dirname(__file__)
    keystore = path + "/KeyStorePracticas"
    ks = jks.KeyStore.load(keystore, "123456")
    for alias, sk in ks.secret_keys.items():
        if sk.alias == "hmac-sha256":
            key = sk.key
    print("La clave es:", key.hex())
    clave = bytes.fromhex(key.hex())


    textoPlano_bytes = bytes('Siempre existe más de una forma de hacerlo, y más de una solución válida.', 'UTF-8')

    hmac256 = HMAC.new(clave, msg=textoPlano_bytes, digestmod=SHA256)
    print(hmac256.hexdigest())


except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)