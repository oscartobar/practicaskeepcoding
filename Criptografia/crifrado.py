from base64 import b64decode
from Crypto.Cipher import DES3,AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

mensaje_original = bytes('KeepCoding es una pasada', 'UTF-8') 
llave = bytes.fromhex("E2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")
iv = bytes.fromhex("00000000000000000000000000000000")

print("Mensaje mensaje_original HEX:", mensaje_original.hex())

# crear un "cifrador"
miCifrador = AES.new(llave, AES.MODE_CBC ,iv)
msg_cifrado_bytes = miCifrador.encrypt(pad(mensaje_original, AES.block_size,style='pkcs7'))
print("Mensaje cifrado HEX:", msg_cifrado_bytes.hex())
print("Mensaje cifrado bytes:", msg_cifrado_bytes)
print("texto cifrado (Base64):", b64encode(msg_cifrado_bytes).decode('utf-8'))

varbase64 = b64encode(msg_cifrado_bytes)
print("varbase64:", varbase64)
vabasutf = varbase64.decode('utf-8')
print("vabasutf:", vabasutf)
#decodificar
