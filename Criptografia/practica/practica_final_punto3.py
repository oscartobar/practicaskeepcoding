from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import jks
import os


# Obteniendo el path
path = os.path.dirname(__file__)

keystore = path + "/KeyStorePracticas"

keystore =  ".\KeyStorePracticas"
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-chacha20-256":
        key = sk.key
print("La clave es:", key.hex())
clave = bytes.fromhex(key.hex())


textoPlano_bytes = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')


#Importante NUNCA debe fijarse el nonce
nonce_mensaje = get_random_bytes(12)
enciptador = ChaCha20.new(key=clave, nonce=nonce_mensaje)
#Por ser cifrado autenticado hacemos un update (lo mismo ocurria en AES-GCM)

texto_cifrado = enciptador.encrypt(textoPlano_bytes)
print("Nonce:", b64encode(nonce_mensaje).decode())
print("Texto Encriptado:", b64encode(texto_cifrado).decode())

#Descifrado...


desenciptador   = ChaCha20.new(key=clave, nonce=nonce_mensaje)
plaintext       = desenciptador.decrypt(texto_cifrado)
print('Mensaje en claro = ',plaintext.decode('utf-8'))