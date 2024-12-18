#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 4B

import jwt
from jwt.exceptions import InvalidSignatureError


try:
 
    decode_jwt = jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI',"Con KeepCoding aprendemos", algorithms="HS256")
    print(decode_jwt)


except ( InvalidSignatureError ) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)