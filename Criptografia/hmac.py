from Crypto.Hash import HMAC, SHA256



def getHMAC(key_bytes,data_bytes):
    hmac256 = HMAC.new(key_bytes, msg=data_bytes, digestmod=SHA256)
    return hmac256.hexdigest()

def validateHMAC(key_bytes,data_bytes,hmac):
    hmac256 = HMAC.new(key_bytes,msg=data_bytes,digestmod=SHA256)
    result = "KO"
    try:
        hmac256.hexverify(hmac)
        result = "OK"
    except ValueError:
        result = "KO"
    print("result: " + result)
    return result


clave_bytes = bytes.fromhex('7212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')
datos = bytes("KeepCoding Mola mucho", "utf8")

hmac = getHMAC(clave_bytes,datos)

print("resultado",hmac)

print(validateHMAC(clave_bytes, datos,hmac))