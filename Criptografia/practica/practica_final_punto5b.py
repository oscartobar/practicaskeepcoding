#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 5b

import hashlib


try:
    generado = '4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833'
    texto_hashear_bytes=bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8") 

    hasheador = hashlib.sha256()
    hasheador.update(texto_hashear_bytes)
    if ( hasheador.digest().hex()) == generado:
        print("El hash es sha256")
    
    hasheador = hashlib.sha224()
    hasheador.update(texto_hashear_bytes)
    if ( hasheador.digest().hex()) == generado:
        print("El hash es sha224")
    
    hasheador = hashlib.sha512()
    hasheador.update(texto_hashear_bytes)
    if ( hasheador.digest().hex()) == generado:
        print("El hash es sha512")
    
    
except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 