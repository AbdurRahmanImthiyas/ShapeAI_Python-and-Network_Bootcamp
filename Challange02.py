import hashlib

message = "My favourite fruit is watermelon"

# hash with SHA-2
print("SHA-256:", hashlib.sha256(message.encode()).hexdigest())

# hash with SHA-3
print("SHA-3-256:", hashlib.sha3_256(message.encode()).hexdigest())

# hash with md5

print("md5:", hashlib.md5(message.encode()).hexdigest())