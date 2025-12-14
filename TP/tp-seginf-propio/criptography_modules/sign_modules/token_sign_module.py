import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# cargamos la clave privada para firmar
with open("priv-key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

def sign_message(message: str) -> str:
    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    signature_b64 = base64.urlsafe_b64encode(signature).decode()
    
    # lo devolvemos en texto plano ? o ciframos ? necesitamos otro par de claves
    return f"{message}.{signature_b64}"
