#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 13B

import ed25519
import os
try:


    my_path = os.path.abspath(os.getcwd())

    fichero_fpriv = my_path + "/ed25519-priv"
    fpriv=open(fichero_fpriv,'rb')
    keypr= fpriv.read()
    fpriv.close()
    
    fichero_fpub = my_path + "/ed25519-publ"
    fpub=open(fichero_fpub,'rb')
    keypublica= fpub.read()
    fpub.close()
    
    
    signedKey = ed25519.SigningKey(keypr)
    msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
    signature = signedKey.sign(msg, encoding='hex')
    
    print("Firma Generada (64 bytes):", signature)
    verifyKey = ed25519.VerifyingKey(keypublica.hex(),encoding="hex")
    verifyKey.verify(signature, msg, encoding='hex')
    print("La firma es válida")


except (ValueError, KeyError) as error: 
    print("Problemas al cifrar....")
    print("El motivo del error es: ", error)