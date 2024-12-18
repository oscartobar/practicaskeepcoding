#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 5

import hashlib


try:
    generado = 'bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe'
    texto_hashear_bytes=bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8") 

    hasheador = hashlib.sha3_256()
    hasheador.update(texto_hashear_bytes)
    if ( hasheador.digest().hex()) == generado:
        print("El hash es sha3_256")
    
    hasheador = hashlib.sha3_384()
    hasheador.update(texto_hashear_bytes)
    if ( hasheador.digest().hex()) == generado:
        print("El hash es sha3_384")
    
    hasheador = hashlib.sha3_512()
    hasheador.update(texto_hashear_bytes)
    if ( hasheador.digest().hex()) == generado:
        print("El hash es sha3_512")    

    hasheador = hashlib.sha3_224()
    hasheador.update(texto_hashear_bytes)
    if ( hasheador.digest().hex()) == generado:
        print("El hash es sha3_224")    

    
    
except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 