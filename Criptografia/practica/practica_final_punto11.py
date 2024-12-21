#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 11

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256,SHA512
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
    
    

    mensajeCifrado=bytes.fromhex("b72e6fd48155f565dd2684df3ffa8746d649b11f0ed4637fc4c99d18283b32e1709b30c96b4a8a20d5dbc639e9d83a53681e6d96f76a0e4c279f0dffa76a329d04e3d3d4ad629793eb00cc76d10fc00475eb76bfbc1273303882609957c4c0ae2c4f5ba670a4126f2f14a9f4b6f41aa2edba01b4bd586624659fca82f5b4970186502de8624071be78ccef573d896b8eac86f5d43ca7b10b59be4acf8f8e0498a455da04f67d3f98b4cd907f27639f4b1df3c50e05d5bf63768088226e2a9177485c54f72407fdf358fe64479677d8296ad38c6f177ea7cb74927651cf24b01dee27895d4f05fb5c161957845cd1b5848ed64ed3b03722b21a526a6e447cb8ee")
    descifrador = PKCS1_OAEP.new(keypr, SHA256)
    decrypted = descifrador.decrypt(mensajeCifrado)
    print("Descifrado: ", decrypted.hex())

    mensaje = decrypted

    encriptador = PKCS1_OAEP.new(keypublica,SHA256)
    text_cifrado = encriptador.encrypt(mensaje)

    print("Cifrado:", text_cifrado.hex())
    print("--------------------------------------------------")



except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)