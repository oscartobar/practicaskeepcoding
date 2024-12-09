from Crypto.Cipher import Salsa20
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes



#Descifrado...
clave           = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
nonce_mensaje   = bytes.fromhex('20a882ea4a57640d')
texto_cifrado   = bytes.fromhex('2340b2ab31df65f1304389930b11b5950b839071f0a97d0e41d51f4f757a')
desenciptador   = Salsa20.new(key=clave, nonce=nonce_mensaje)
plaintext       = desenciptador.decrypt(texto_cifrado)

print('Mensaje en claro = ',plaintext.decode('utf-8'))