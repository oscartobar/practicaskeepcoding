#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 2a


from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import jks
import os


# Obteniendo el path
path = os.path.dirname(__file__)

keystore = path + "/KeyStorePracticas"
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        key = sk.key
print("La clave es:", key.hex())
clave = bytes.fromhex(key.hex())

# Descifrado
try:
    iv_bytes = bytes.fromhex("00000000000000000000000000000000")
    texto_cifrado_entregado = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
    texto_cifrado_b64 = b64decode(texto_cifrado_entregado)
    descifrador = AES.new(clave, AES.MODE_CBC, iv_bytes)
    texto_descifrado = unpad(descifrador.decrypt(texto_cifrado_b64), AES.block_size, style="pkcs7")
    print("Texto descifrado:", texto_descifrado.decode("utf-8"))
except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 