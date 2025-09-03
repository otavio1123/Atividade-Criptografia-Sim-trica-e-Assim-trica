import os, base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Geração da chave secreta compartilhada entre Cliente e Empresa
chave = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(chave)


mensagem = b"Mensagem secreta do Cliente para a Empresa"

# Nonce valor único por cifragem
nonce = os.urandom(12)

# Cliente cifra a mensagem
cifrado = aesgcm.encrypt(nonce, mensagem, None)

# Empresa decifra usando a mesma chave e nonce
decifrado = aesgcm.decrypt(nonce, cifrado, None)

print("\n=== Criptografia Simétrica (AES-GCM) ===")
print("Chave (Base64):", base64.b64encode(chave).decode())
print("Nonce (Base64):", base64.b64encode(nonce).decode())
print("Ciphertext (Base64):", base64.b64encode(cifrado).decode())
print("Texto decifrado:", decifrado.decode())
