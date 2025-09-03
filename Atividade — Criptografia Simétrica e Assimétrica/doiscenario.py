from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 1. Criptografia Simétrica

print("=== Criptografia Simétrica (AES/Fernet) ===")

# Gerar chave
chave_simetrica = Fernet.generate_key()
fernet = Fernet(chave_simetrica)

mensagem = b"Dados confidenciais do cliente"

# Cifrar
cifrado = fernet.encrypt(mensagem)
# Decifrar
decifrado = fernet.decrypt(cifrado)

print(f"Chave simétrica (deve ser mantida em segredo): {chave_simetrica}")
print(f"Mensagem original: {mensagem}")
print(f"Mensagem cifrada: {cifrado}")
print(f"Mensagem decifrada: {decifrado}\n")



# 2. Criptografia Assimétrica

print("=== Criptografia Assimétrica (RSA) ===")

# Gerar par de chaves privada + pública
chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

chave_publica = chave_privada.public_key()

mensagem2 = b"Mensagem secreta do cliente para a empresa"

# Cifrar com chave pública
cifrado2 = chave_publica.encrypt(
    mensagem2,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decifrar com chave privada
decifrado2 = chave_privada.decrypt(
    cifrado2,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Exportar chave pública em PEM (poderia ser compartilhada)
chave_publica_pem = chave_publica.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(f"Chave pública (pode ser distribuída):\n{chave_publica_pem.decode()}")
print(f"Mensagem original: {mensagem2}")
print(f"Mensagem cifrada: {cifrado2}")
print(f"Mensagem decifrada: {decifrado2}")
