#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 3B

from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import jks
import os

try:

    # Obteniendo el path
    path = os.path.dirname(__file__)
    keystore = path + "/KeyStorePracticas"
    ks = jks.KeyStore.load(keystore, "123456")
    for alias, sk in ks.secret_keys.items():
        if sk.alias == "cifrado-sim-chacha20-256":
            key = sk.key
    print("La clave es:", key.hex())
    clave = bytes.fromhex(key.hex())


    textoPlano_bytes = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')

    #Importante NUNCA debe fijarse el nonce
    nonce_mensaje = get_random_bytes(12)
    enciptador = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    #Por ser cifrado autenticado hacemos un update (lo mismo ocurria en AES-GCM)
    datos_asociados = bytes('Id=54', 'utf-8')
    cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    cipher.update(datos_asociados)
    texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano_bytes)    

    print("Nonce:", b64encode(nonce_mensaje).decode())
    print("Texto Encriptado:", b64encode(texto_cifrado).decode())
    print("Texto Encriptado:", b64encode(tag).decode())

    #Descifrado...
    desenciptador   = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    desenciptador.update(datos_asociados)
    plaintext       = desenciptador.decrypt_and_verify(texto_cifrado,tag)
    print('Mensaje en claro = ',plaintext.decode('utf-8'))
except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)