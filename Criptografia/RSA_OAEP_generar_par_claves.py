from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import os

my_path = os.path.abspath(os.getcwd())


#Vamos a generar las claves en vuelo
keyPair = RSA.generate(2048) #Definimos clave publica y privada.

pubKey = keyPair.publickey()
privkey = keyPair.exportKey()

fichero_pub = my_path + "\clavePublica-RSA.pem"
f=open(fichero_pub,'wb')
f.write(pubKey.export_key())
f.close()
print(pubKey.export_key().decode('utf8'))

fichero_priv = my_path + "\clavePrivada-RSA.pem"
f2=open(fichero_priv,'wb')
f2.write(privkey )
f2.close()
print(privkey.decode('utf8'))


