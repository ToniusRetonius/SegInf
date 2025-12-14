FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos el proyecto
COPY . .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto del server
EXPOSE 9999

# Comando por defecto
CMD ["python3", "server.py"]
