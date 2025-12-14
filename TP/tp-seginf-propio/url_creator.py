from criptography_modules.sign_modules.token_sign_module import sign_message

def create_url():
    message = "honey123"
    # ciframos el mensaje ? Es esencial ? o sólo con firmarlo alcanza ?
    token = sign_message(message)
    url = f"http://localhost:9999/{token}"
    return url