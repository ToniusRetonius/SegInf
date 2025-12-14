from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# necesitamos que el server conozca la pública
with open('pub-key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(f.read())

class handlerHoneyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        token = self.path.strip("/")

        if "." not in token:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Invalid token format\n")
            return

        message, signature_b64 = token.split(".", 1)

        try:
            signature = base64.urlsafe_b64decode(signature_b64)

            # Verificamos la firma
            public_key.verify(
                signature,
                message.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )

            print(f'[ALERTA] Token activado: {token} desde IP {self.client_address[0]}')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK.\n')
        except Exception as e:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found.\n')
            # DEBUG
            print(f"[ERROR] Falló verificación: {e}")
            print(f"[DEBUG] Token recibido: {token}")
            print(f"[DEBUG] Message: {message}")
            print(f"[DEBUG] Signature (base64): {signature_b64}")

if __name__ == "__main__":
    print('Servidor corriendo en http://0.0.0.0:9999')
    server = HTTPServer(("0.0.0.0", 9999), handlerHoneyServer)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Servidor frenó')