#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 5c

import hashlib


try:
    #Texto a hashear
    texto_hashear_bytes=bytes("En KeepCoding aprendemos cómo protegernos con criptografía.", "utf8") 

    hasheador = hashlib.sha3_256()
    hasheador.update(texto_hashear_bytes)
    print("El hash es sha3_256 bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe")
    print("El hash es sha2_512 4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833")
    print("El hash es sha3_256: "+hasheador.digest().hex())
    
    
except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 