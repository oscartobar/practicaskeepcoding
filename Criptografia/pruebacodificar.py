import base64
Componente1 = 0xAFAA1232BCFF
Componente2 = 0xBCAA3332BCFA
print(hex(Componente1^Componente2))
print(Componente1^Componente2)

cadena = base64.standard_b64decode("Vml2YSBLZWVwQ29kaW5n")
print (cadena)
cadena = base64.b64decode("Vml2YSBLZWVwQ29kaW5n")
print (cadena)

tres = 'Viva KeepCoding'
print(bytes(tres, 'utf-8').hex())

