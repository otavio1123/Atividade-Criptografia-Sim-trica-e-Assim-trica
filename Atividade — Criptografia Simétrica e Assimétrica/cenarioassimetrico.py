import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Empresa gera um par de chaves pública e privada
chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
chave_publica = chave_privada.public_key()


mensagem = b"Mensagem secreta do Cliente para a Empresa"

# Cliente cifra com a chave pública da Empresa
cifrado = chave_publica.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Empresa decifra com sua chave privada
decifrado = chave_privada.decrypt(
    cifrado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\n=== Criptografia Assimétrica (RSA-OAEP) ===")
print("Ciphertext (Base64):", base64.b64encode(cifrado).decode())
print("Texto decifrado:", decifrado.decode())
