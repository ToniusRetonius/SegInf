import os
from criptography_modules.key_generator_modules.priv_pub_key_generator import private_key, public_key  

import argparse
from token_generator_modules.pdf_token_generator import create_pdf_token
from token_generator_modules.url_token_generator import create_url_token
from token_generator_modules.qr_token_generator import create_qr_token

def main():
    # creamos el parser
    parser = argparse.ArgumentParser(description="Interfaz de creación de honeytokens")
    
    # definimos los argumentos (--type y --output)
    parser.add_argument("--type", required=True, choices=['url', 'qr', 'pdf'], help="Tipo de honeytoken")
    parser.add_argument("--output", required=True, help="Archivo de salida")

    # argumentos capturados
    args = parser.parse_args()
    token_type = args.type
    output_name_file = args.output

    # sanitizamos ? o con choices ya está ?

    # según el type, decidimos qué hacer :
    if token_type == 'pdf':
        create_pdf_token()
    elif token_type == 'qr':
        create_qr_token()
    elif token_type == 'url':
        create_url_token()

if __name__ == "__main__":
    main()
