#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 1b

fija = int('B1EF2ACFE2BAEEFF', 16)
clavekeymanager = int('B98A15BA31AEBB3F',16)
print("Clave Fija",hex(fija)[2:].upper())
print("Clave clavekeymanager",hex(clavekeymanager)[2:].upper())
fijaXorclavekeymanager = fija^clavekeymanager
print("Clave en Memoria",hex(fijaXorclavekeymanager)[2:].upper())

