# import qrcode
from criptography_modules.sign_modules.token_sign_module import sign_message

def create_qr_token(output="honey.png"):
    message = "qr123"
    # token = sign_message(message)
    # url = f"http://localhost:9999/{token}"
    # img = qrcode.make(url)
    # img.save(output)
    print(message)
    # print(f"QR creado: {output}")
