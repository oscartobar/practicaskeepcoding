import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


#Cifrado
textoPlano_bytes = bytes('He descubierto el error y no volveré a hacerlo mal', 'UTF-8')
datos_asociados_bytes = bytes("validar la integridad y la autenticación", "UTF-8")

clave = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')

nonceDinamico = get_random_bytes(12) 
datos_asociados_bytes = bytes("frase de seguridad.", "UTF-8")


encriptador = AES.new(clave, AES.MODE_GCM,nonce=nonceDinamico)
encriptador.update(datos_asociados_bytes)
texto_cifrado_bytes, tag = encriptador.encrypt_and_digest(textoPlano_bytes)
tag_b64 =b64encode(tag).decode('utf-8')


#Descifrado

try:
    tag_desc_bytes = b64decode(tag_b64)
    cipher = AES.new(clave, AES.MODE_GCM, nonce=nonceDinamico)
    cipher.update(datos_asociados_bytes)
    mensaje_des_bytes = cipher.decrypt_and_verify(texto_cifrado_bytes,tag_desc_bytes)
    
    mensaje_des_base64hex = b64encode(mensaje_des_bytes).hex()
    #print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))
    print("El texto en Haxadecimal y Base64: ", mensaje_des_base64hex )

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 