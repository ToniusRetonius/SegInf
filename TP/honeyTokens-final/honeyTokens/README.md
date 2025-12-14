# Pasos para correr con Docker
1. Hacemos el build desde el directorio raiz.
````bash
sudo docker-compose up --build 
`````
*En caso de no tener el docker-compose (me pasó) ->
```bash
sudo apt install docker-compose
```
2. Cuando termina el build, vamos a tener el server corriendo, tenemos que hacer el attach desde otra terminal 
````bash
sudo docker attach honey-cli
````
Para luego poder hacer uso de la CLI.
