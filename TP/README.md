## Manual de uso

### Ejecución del sistema con Docker

A continuación se describen los pasos necesarios para ejecutar el sistema utilizando contenedores Docker.

1. **Build y levantado de los contenedores**

   Desde el directorio raíz del proyecto se debe ejecutar el siguiente comando:
```bash
sudo docker-compose up --build
```
    En caso de no contar con *docker-compose* instalado, puede instalarse mediante:
```bash
sudo apt install docker-compose
```
2. Acceso a la aplicación CLI

    Una vez finalizado el proceso de build, el servidor queda en ejecución.
    Para interactuar con la aplicación CLI, se debe abrir una nueva terminal y realizar el attach al contenedor correspondiente:
```bash
   sudo docker attach honey-cli
```
    A partir de este punto, el usuario puede utilizar los comandos de la CLI para generar honeytokens.

## Generación de HoneyTokens
A partir del comando *generate*, se pueden crear distintos tipos de honeytokens según el uso deseado. (Ver más información sobre el uso en la sección de *Manual de uso y prueba* del informe). Según corresponda, los archivos creados estarán disponibles en *app/generated*.

### URL
```bash
   generate url --mail usuario@mail.com --message "texto"
```
### QR
```bash
   generate qr --mail usuario@mail.com --message "texto" --nameFile "name"
```
### WebImage
```bash
   generate webImage --mail usuario@mail.com --message "texto" --image image.png
```
### Word (.docx)
```bash
   generate word --mail usuario@mail.com --message "texto"
```
### Credentials
```bash
   generate Credentials --mail usuario@mail.com --message "texto" --nameFile "name"
```
