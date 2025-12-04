# TP - Seginf

Tenemos que crear una interfaz de consola (CLI) que nos permita crear honeytokens con distintas tecnología (**generator**) y un **servidor de alertas** donde tenemos dos endpoints (uno para registrar los tokens y otro para recibir los GET (se debe registrar fecha/hora, IP origen y tipo de token)).
La idea es que pueda recibir ciertos parámetros por consola como *--type* para decidir desde la consola qué tipo de honeytoken generar y *--output* para decir el nombre del archivo. Por ejemplo:
````bash
python3 token-snare-cli.py --type pdf --output carnada.pdf
````

## Primer paso - CLI
### Lo más simple posible
Creamos una CLI simple que capture los argumentos:
````python
import argparse
def main():
    parser = argparse.ArgumentParser(description="Interfaz de creación de honeytokens")
    parser.add_argument("--type", required=True, choices=['url','qr','pdf'] help="Tipo de honeytoken")
    parser.add_argument("--output", required=True, help="Archivo de salida")
    args = parser.parse_args()
````
### Separación de responsabilidades
A continuación tenemos que decidir si se trata de un *pdf, qr, url,..* por tanto, tenemos que armar la estructura de ifs
````python
if args.type == 'pdf':
    create_pdf_token()
elif ...
````

## Segundo paso - Server 
### Lo más simple posible
Necesitamos crear un servidor simple que sea capaz de capturar cuando se hace un *GET* a la url del honeytoken. Entonces, *asumamos que el servidor conoce la URL inicialmente*. 
Definimos  : 

TOKENS = set('honey')

Corremos desde una terminal :
python3 server.py 
Servidor corriendo en http://localhost:9999

desde otra terminal hacemos un *curl http://localhost:9999/honey*

Como consecuencia, el servidor loggea :

[ALERTA] Token activado: honey desde IP 127.0.0.1
127.0.0.1 - - [03/Dec/2025 12:59:10] "GET /honey HTTP/1.1" 200 -

### Ahora la idea es que el servidor no tenga hardcodeada la url
La idea es que haya una comunicación entre la *CLI <-> Server*. O sea, como queremos crear el honeytoken, el server tiene que conocer la url ya que sino, cómo sabe qué url es la que recibió la petición. Por tanto, tenemos que decidir qué mecanismo usamos :
- Un archivo *tokens.txt* que tiene las url de los tokens
- Token firmado como usa Canary Tokens. La idea es que la CLI genera algo como *http://localhost:9999/TOKEN_ENCRIPTADO*

### Vamos a usar el mecanismo de url firmada 
Si nuestro *server* cuando recibe la petición, puede constatar la firma, es porque es un honeytoken, sino, no. La idea es implementar los *módulos de criptografía*

## Módulos de criptografía
Tenemos que crear la funciones de *cifrado/descifrado* y tenemos que generar el par de claves. 

### Cargar claves
- A la CLI tenemos que cargarle la privada para que al crear la URL pueda cifrarla :
````python
with open('priv-key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)
    
````
- Al server le tenemos que facilitar la *pública* para descifrar el cacho final de la URL.
Para eso, le agregamos al principio :
````python
with open('pub-key.pem', 'rb') as f:
    public_key = serialization.load_pe_public_key(f.read())
````
### Al final, me pareció que podemos hacer una firma nomás, en vez de garantizar confidencialidad
Por tanto, las funciones de cifrado y descifrado se deprecan. Hacemos uso de las verificaciones desde el server. El usuario genera el honeytoken y firma la url con su privada y luego el servidor autentica, si puede, y con ello garantiza que recibió una petición *GET* para cierta url. 


## Probando 

### URL
Lo primero es probarla localmente desde dos terminales distintas:

- python3 cli.py --type url --output e

URL generada:
http://localhost:9999/honey123.pQ3jMxeQrT4tpcXObEo3yoSBGo4SiP-VHFsgLyCPLknPjLkR-mCDOq2_w7KYtGXO4Q2u8nnCOM4wdT2P6nYW3y9Pasz2yocpP-cs3GVE5tkg2IKq7l2uLbxohlQCHqqEMvsHWLc96U9JQYIIpOHGKfRLrRNNf5uNFaeJQUye99WgD9AslkEyXYp3mhbdUxblmHfFZHbWnvZCbGvLcfI3RQqhPMEOW9qPO9yQoLcnKiKAfcqE7eeMIEIzlrsPdHqYKygUktxqkRsijM5xY_5N2muw0dsT_ZCOYvkeOunjL0Tqf6Sc4A0ou3HsArUyGX5O2nL_ozkhtJ4Br31USV9MDA==

- python3 server.py 
Servidor corriendo en http://localhost:9999
[ALERTA] Token activado: honey123.pQ3jMxeQrT4tpcXObEo3yoSBGo4SiP-VHFsgLyCPLknPjLkR-mCDOq2_w7KYtGXO4Q2u8nnCOM4wdT2P6nYW3y9Pasz2yocpP-cs3GVE5tkg2IKq7l2uLbxohlQCHqqEMvsHWLc96U9JQYIIpOHGKfRLrRNNf5uNFaeJQUye99WgD9AslkEyXYp3mhbdUxblmHfFZHbWnvZCbGvLcfI3RQqhPMEOW9qPO9yQoLcnKiKAfcqE7eeMIEIzlrsPdHqYKygUktxqkRsijM5xY_5N2muw0dsT_ZCOYvkeOunjL0Tqf6Sc4A0ou3HsArUyGX5O2nL_ozkhtJ4Br31USV9MDA== desde IP 127.0.0.1
127.0.0.1 - - [04/Dec/2025 13:34:29] "GET /honey123.pQ3jMxeQrT4tpcXObEo3yoSBGo4SiP-VHFsgLyCPLknPjLkR-mCDOq2_w7KYtGXO4Q2u8nnCOM4wdT2P6nYW3y9Pasz2yocpP-cs3GVE5tkg2IKq7l2uLbxohlQCHqqEMvsHWLc96U9JQYIIpOHGKfRLrRNNf5uNFaeJQUye99WgD9AslkEyXYp3mhbdUxblmHfFZHbWnvZCbGvLcfI3RQqhPMEOW9qPO9yQoLcnKiKAfcqE7eeMIEIzlrsPdHqYKygUktxqkRsijM5xY_5N2muw0dsT_ZCOYvkeOunjL0Tqf6Sc4A0ou3HsArUyGX5O2nL_ozkhtJ4Br31USV9MDA== HTTP/1.1" 200 -

### Docker
Para poder empaquetar todo el entorno en una imagen reproducible y que siempre funcione en cualquier máquina, vamos a construir nuestro proyecto con Docker.
Los pasos son simples :
1. Generamos el Dockerfile en la raiz del proyecto (son instrucciones)
    - *FROM python:3.12-slim* : Construí esta imagen a partir de otra imagen base que ya trae Python 3.12 (slim es para que sea la versión liviana)


    - *WORKDIR /app* : definime como directorio de trabajo dentro del contenedor el /app

    - *COPY . .* : copiá todo el proyecto al contendor

    - *RUN pip install --no-cache-dir -r requirements.txt* : corré un comando durante el buil de la imagen para instalar todas las dependencias que escribí en el txt *requierements* y no las guardes en cache (más liviano)

    - *EXPOSE 9999* : declará que el puerto interno donde mi proyecto escuchará será el 9999, o sea, no lo expone pero le decimos que nuestro proyecto usará ese. Después explico cómo hacemos realmente uso de esto


    - *CMD ["python3", "server.py"]* : comando por defecto a penas arranca el contenedor, es análogo a correr en la terminar *python3 server.py*

2. Hacemos el build del proyecto
`````bash
sudo docker build -t honeytokens .
`````
Construir una imagen a partir del Dockerfile en el directiorio actual (por eso el punto al final) y le ponemos nombre (-t) *honeytokens* 

3. Corremos el contenedor
`````bash
sudo docker run -p 9999:9999 honeytokens
`````
Ahora sí, creá y ejecutá el contenedor a partir de la imagen llamada *honeytokens* y **mapeame los puertos (-p) 9999:9999** donde **<puerto_host>:<puerto_contenedor>**. O sea, como dijimos antes que nuestro proyecto usa ese puerto, tenemos que mapear correctamente la del host y la del contenedor. Esto es fundamental para poder acceder al contenedor desde fuera, ya que sino queda aislado.


### QR 
Para el caso del qr tenemos que probarlo en un entorno virtual de python así que, copio la carpeta y hago las pruebas
`````bash
python3 -m venv venv
source venv/bin/activate
`````
Después de activarlo tenemos que ver algo como :
(venv) .../prueba
`````bash
pip install -r requierements.txt
`````
