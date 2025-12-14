from criptography_modules.sign_modules.token_sign_module import sign_message
from url_creator import create_url
def create_url_token():
    url = create_url()
    print("\nURL generada:")
    print(url)
    return url