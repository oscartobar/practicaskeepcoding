from base64 import b64decode
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode


llave = bytes.fromhex("2b7e151628aed2a6abf715891defefef123456781232aaff")
iv = bytes.fromhex("1010011111111111")



# descifrador
            
mensaje_bytes_encriptado = bytes.fromhex("2b6911293fc8a5733170c5e1b3f43c6ee51285f679b1f3112f1a628382a5794a")


descifrador = DES3.new(llave, DES3.MODE_CBC,iv)
msg_reto = descifrador.decrypt(mensaje_bytes_encriptado)
msg_claro = unpad(msg_reto, DES3.block_size, style='pkcs7')
print("Mensaje DEScifrado HEX:", msg_reto.hex())
print("Mensaje DEScifrado Bytes:", msg_reto)
print("Mensaje DEScifrado  UTF8:", msg_reto.decode('utf-8'))
print("Mensaje DEScifrado SP HEX:", msg_claro.hex())
print("Mensaje DEScifrado SP Bytes:", msg_claro)
print("Mensaje DEScifrado SP UTF8:", msg_claro.decode('utf-8'))

