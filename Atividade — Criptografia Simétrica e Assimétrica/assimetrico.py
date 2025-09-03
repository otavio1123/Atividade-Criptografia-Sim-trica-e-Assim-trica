import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

#  Gerar par de chaves pública e privada
chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
chave_publica = chave_privada.public_key()

# Mensagem a cifrar
mensagem = input("Digite a mensagem a cifrar: ").encode()

#  Cifrar com a chave pública
ciphertext = chave_publica.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

#  Decifrar com a chave privada
texto_decifrado = chave_privada.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)


print("\n=== RESULTADOS ===")
print("Ciphertext (Base64):", base64.b64encode(ciphertext).decode())
print("Texto decifrado:", texto_decifrado.decode())


