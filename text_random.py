from utils_app.cryptography import CryptographyToken


cryptographyToken = CryptographyToken()

token_to_encrypt = "hello my name is david solis"


decrypt_1 = cryptographyToken.encrypt_token("1")
decrypt_c = cryptographyToken.encrypt_token("20200938")

print(decrypt_1)
print("")
print(decrypt_c)
