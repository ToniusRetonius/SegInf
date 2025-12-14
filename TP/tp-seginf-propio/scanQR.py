from pyzbar.pyzbar import decode
from PIL import Image
import webbrowser
import sys

# Verificar que pasaron un archivo
if len(sys.argv) < 2:
    print("Uso: python scanQR.py <archivo_imagen>")
    sys.exit(1)

archivo = sys.argv[1]

# Abrir imagen y decodificar
img = Image.open(archivo)
codes = decode(img)

if not codes:
    print('No se encontró QR en la imagen.')
    sys.exit(1)

# Convertir bytes a string
link = codes[0].data.decode('utf-8')

print("Link detectado:", link)
webbrowser.open(link)
