import qrcode
from url_creator import create_url

def create_qr_token(file_name):  
    honey_url = create_url()
    img = qrcode.make(honey_url)
    img.save(file_name)
    print(f"\n[OK] QR generado correctamente : {file_name}")