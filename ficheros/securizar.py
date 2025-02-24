import hashlib

password = "estaEsMiContraseña"
hash = hashlib.sha256(password.encode()).hexdigest()

print(password)
print(hash)