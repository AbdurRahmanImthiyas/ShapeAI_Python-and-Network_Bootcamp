import hashlib, os

message = "My favourite fruit is watermelon"

message = message.encode()

salt = os.urandom(16)

sha256_hash = hashlib.pbkdf2_hmac("sha256", message, salt, 100000)
sha3_hash = hashlib.pbkdf2_hmac("sha3_256", message, salt, 100000)
md5_hash = hashlib.pbkdf2_hmac("md5", message, salt, 100000)

print("SHA-256:",sha256_hash)
print("SHA-3-256:",sha3_hash)
print("md5:",md5_hash)