from flask import Flask, request
import uuid

app = Flask(__name__)

# Generamos un token único
TOKEN = uuid.uuid4().hex
print(f"Honeytoken listo: http://127.0.0.1:5000/{TOKEN}")

# cuando llegue una petición GET a /<valor del TOKEN> ejecutá la función honey :
@app.route(f"/{TOKEN}")
def honey():
    # acá implementar la lógica de la alerta !!

    # Extrae la IP remota que hizo la petición desde el objeto request.
    ip = request.remote_addr
    
    print(f"Honeytoken activado por IP: {ip}")
    
    # Devuelve una respuesta HTTP al cliente: cuerpo "Recurso no disponible" y código de estado 200 OK.
    return "Recurso no disponible", 200

