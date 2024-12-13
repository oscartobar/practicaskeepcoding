from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA3_512
import os



fichero_priv =  "clavePrivada-RSA.pem"
# Carga de la clave privada
with open(fichero_priv, 'r') as f:
    keypriv = RSA.import_key(f.read())

# Carga del texto cifrado desde el archivo
fichero_cifrado = "textoencriptado.txt"
with open(fichero_cifrado, 'rb') as f:
    mensajeCifrado = f.read()

#mensajeCifrado=bytes.fromhex("4c8d764fddc8f37af79d1d015f4c17768f4fcbdb64e2ca8266abaa33c427090f2e6947587f3d9b1946dc310d96c03aa6a507d929b10e3651370cdacb1c535140908ba72383f95f6491f36c0eb46f2abfebc51ada47737a2e4a520821fe57d99e3f2eef7e95bf615d4ae9f0cfefc1d43c340611073c1c32e4b916e2687604997782d4a822beb4506cd40f9a8c72fd1b1e330cadb1ff697d2a3d24bf12f8fbd23958962f68b6b54eff4c4f03ee233d450ed7a23d330fb8ab34ccf281aa011f37364b2458264ae5fbdb3dd69da130e3799b25ffe7a247885f651078095fd3ed481cd57d92db0bc48d330ad8bf0dc56dfa130f52520e90a9f1af76b0c66d48e17c69")
descifrador = PKCS1_OAEP.new(keypriv, SHA3_512)
decrypted = descifrador.decrypt(mensajeCifrado)
print("Descifrado: ", decrypted.decode('utf-8'))






