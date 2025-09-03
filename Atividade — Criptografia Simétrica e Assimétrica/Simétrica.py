import os, base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Entrada da mensagem
mensagem = input("Digite a mensagem a cifrar (ex.: Dados confidenciais do cliente): ")

# Gera uma chave simétrica de 256 bits (32 bytes)
chave = AESGCM.generate_key(bit_length=256)

# Gera um nonce (vetor único de inicialização) de 12 bytes
nonce = os.urandom(12)

# Cria objeto AES-GCM com a chave
aesgcm = AESGCM(chave)

# Cifra a mensagem
ciphertext = aesgcm.encrypt(nonce, mensagem.encode(), None)

# Decifra para testar
texto_decifrado = aesgcm.decrypt(nonce, ciphertext, None).decode()


print("\n=== RESULTADOS ===")
print("Chave (BASE64):", base64.b64encode(chave).decode())
print("Nonce (BASE64):", base64.b64encode(nonce).decode())
print("Ciphertext (BASE64):", base64.b64encode(ciphertext).decode())
print("Texto decifrado:", texto_decifrado)
