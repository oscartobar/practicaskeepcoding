from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

#descifrar el chacha20-poly1305 que te paso por aqui
Mensaje=  {"nonce": "Nro+uMfo7zRFUNC2", "datos asociados": "SWQ9NTQ=", "texto cifrado": "xw1VN6ni65pYm3UJejYhA3v6QkNxD+j2RbT/GMxyJtXUMw6O", "tag": "6gEe1tvr9lLHTApnlXwYYg=="}
clave = bytes.fromhex('d936108299307d3f6f7585b96013346d043f3920b03284c6b45253fd51a545da')
nonce_mensaje   = b64decode(Mensaje["nonce"])
texto_cifrado   = b64decode(Mensaje["texto cifrado"])


#Descifrado...



desenciptador   = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
desenciptador.update(Mensaje["datos asociados"])
plaintext       = desenciptador.decrypt(texto_cifrado)

print('Mensaje en claro = ',plaintext.decode('utf-8'))