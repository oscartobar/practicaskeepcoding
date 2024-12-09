#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 1

fija = int('B1EF2ACFE2BAEEFF', 16)
clavefinal = int('91BA13BA21AABB12',16)
print("Clave Fija",hex(fija)[2:].upper())
print("Clave final",hex(clavefinal)[2:].upper())
fijaXorclavefinal = fija^clavefinal
print("Clave en el Key Manager",hex(fijaXorclavefinal)[2:].upper())

#prueba de XOR
prueba1=fijaXorclavefinal^fija
print("Prueba keymanager con la fija (clavefinal):", hex(prueba1)[2:].upper())

#prueba de XOR
prueba2=fijaXorclavefinal^clavefinal
print("Prueba keymaneger con la clavefinal (fija)= ",hex(prueba2)[2:].upper())

