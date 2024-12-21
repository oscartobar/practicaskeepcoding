#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 15

from psec import tr31

try:

    header, key = tr31.unwrap( kbpk=bytes.fromhex("A1A10101010101010101010101010102"), key_block="D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B")
    print("Clave=", key.hex())
    print("Key Version ID: " + header.version_id )
    print("Algoritmo: " + header.algorithm)
    print("Modo de uso: " + header.mode_of_use)
    print("Uso de la clave: " + header.key_usage)
    print("Exportabilidad: " + header.exportability)
    
    

   



except (ValueError, KeyError) as error: 
   
    print("El motivo del error es: ", error)