from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA3_512
import os

my_path = os.path.abspath(os.getcwd())
fichero_pub = my_path + "\clavePublica-RSA.pem"
f=open(fichero_pub,'r')
keypub= RSA.import_key(f.read())
f.close()
mensaje = "hola mundo"
mensaje_bytes = mensaje.encode('utf-8')

cifrador = PKCS1_OAEP.new(keypub,SHA3_512)
text_cifrado = cifrador.encrypt(mensaje_bytes)

fichero =  "textoencriptado.txt"
f=open(fichero,'wb',encoding='utf-8')
f.write(text_cifrado)
f.close()

print("Cifrado:", text_cifrado.hex())
print("--------------------------------------------------")

