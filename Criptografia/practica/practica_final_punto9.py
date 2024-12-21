#KeepCoding Bootcamp Ciberseguridad | Edición IX
#Informe Practica Criptografia
#Realizado por: Oscar Tobar Rios
#Solucion Punto 9

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def calcular_kcv_sha256(llave_texto: str) -> str:
    # Convertir la clave AES de hexadecimal a bytes
    llave_bytes = bytes.fromhex(llave_texto)
    # Calcular el hash SHA-256
    sha256_hash = SHA256.new(llave_bytes).digest()
    # Tomar los primeros 3 bytes del hash SHA-256
    kcv_sha256 = sha256_hash[:3]
    # Devolver el KCV en formato hexadecimal
    return kcv_sha256.hex().upper()

def calcular_kcv_aes(llave_texto: str) -> str:
    # Convertir la clave AES de hexadecimal a bytes
    llave_bytes = bytes.fromhex(llave_texto)
    # Ceros binarios
    iv = bytes.fromhex("00000000000000000000000000000000") 
    # Inicializar el cifrador AES en modo ECB
    bloqueceros = bytes.fromhex("00000000000000000000000000000000") # Ceros binarios
    
    cipher = AES.new(llave_bytes, AES.MODE_CBC,iv)
    # Cifrar el bloque de ceros
    bloque_encriptado = cipher.encrypt(bloqueceros)
    # Tomar los primeros 6 bytes del bloque cifrado como KCV
    kcv = bloque_encriptado[:6]
    # Devolver el KCV en formato hexadecimal
    return kcv.hex().upper()
    
try:

    
    aes_key = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"

    kcv = calcular_kcv_sha256(aes_key)
    print("KCV SHA256: "+kcv)
    
    kcv = calcular_kcv_aes(aes_key)
    print("KCV AES: "+kcv)
except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)