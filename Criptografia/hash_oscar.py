import hashlib
'''

m = hashlib.md5()
m.update(bytes("Hola", "utf8"))
print("md5:    " + m.digest().hex())

m = hashlib.sha1()
m.update(bytes("Hola", "utf8"))
print("SHA1:   " + m.digest().hex())

m = hashlib.sha256()
m.update(bytes("Hola", "utf8"))
print("SHA256: " + m.digest().hex())
'''
m = hashlib.sha3_512()
m.update(bytes("KeepCoding Mola mucho", "utf8"))
print("SHA3512: " + m.digest().hex())

#  KeepCoding Mola mucho: SHA3512: 2fbd4af1a283ae66edda02ec908b0765ad67d186fd1d4360fbf6b95279ead4ed0a91b0b5ce90aedd5116147f4a0189950c8b6e6c69b304a0a6bd3f698b926e42
#y KeepCoding Mola Mucho: SHA3512: 51a8c0338212c262494436980d90342e7384d89c717b789ed3a5fed538f279ccf6d109cf0a2203405c447e70e93c46f99e744f3a9b36cfb71e568ad12e9093e5