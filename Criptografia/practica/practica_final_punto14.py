#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 14
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets
import os,jks

try:

    # Obteniendo el path
    path = os.path.dirname(__file__)
    keystore = path + "/KeyStorePracticas"
    ks = jks.KeyStore.load(keystore, "123456")
    for alias, sk in ks.secret_keys.items():
        if sk.alias == "cifrado-sim-aes-256":
            key = sk.key
    
    clave = bytes.fromhex(key.hex())

    salt = secrets.token_bytes(16)
    master_secret = bytes.fromhex('e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3')
    key1, key2 = HKDF(master_secret, 32, salt, SHA512, 2)
    
    print("La clave es:", master_secret.hex())
    print("Clave key1: ", key1.hex())
    print("Clave key2: ", key2.hex())



except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)