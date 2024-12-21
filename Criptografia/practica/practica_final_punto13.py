#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 13

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import os


try:


    my_path = os.path.abspath(os.getcwd())

    fichero_fpriv = my_path + "/clave-rsa-oaep-priv.pem"
    fpriv=open(fichero_fpriv,'r')
    keypr= RSA.import_key(fpriv.read())
    fpriv.close()
    
    fichero_fpub = my_path + "/clave-rsa-oaep-publ.pem"
    fpub=open(fichero_fpub,'r')
    keypublica= RSA.import_key(fpub.read())
    fpub.close()
    
    
    mensaje_bytes = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.","utf-8")
    hash = SHA256.new(mensaje_bytes)

    signer=PKCS115_SigScheme(keypr)
    firma = signer.sign(hash)
    print("Firma: ", firma.hex())


except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)