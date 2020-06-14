# Python/Flask - API Hello
Esta es una simple API construida con el lenguaje de programación Python y su framework Flask, con la finalidad de ser levantada en un contenedor docker local, para terminar siendo subida al docker hub público.
### :: Clonar repositorio
```
$ clone https://github.com/galvarezdevs/python-api-hello.git
```
### :: Crear imagen python con framework flash
```
$ docker build -t img-python-api-hello:1.0 -f docker/dockerfile.dev .
```
### :: Verificar que la imagen esta creada en local
```
$ docker images

> resultado:
-------------------- --- ------------
REPOSITORY           TAG IMAGE ID
-------------------- --- ------------
img-python-api-hello 1.0 xyzXYZabcABC
-------------------- --- ------------
```
### :: Levantar contenedor con la imagen python
```
$ docker run -i -t -d --rm -v ${PWD}/src:/app -p 5050:4040 --name cnt-python-api-hello img-python-api-hello:1.0

> resultado (id interno del contenedor):
xyzXYZabcABCxyzXYZabcABCxyzXYZabcABCxyzXYZabcABC
```
### :: Verificar que el contenedor esta en ejecución
```
$ docker ps

> resultado:
------------ ------------------------     ---------------------- --------------------
CONTAINER ID IMAGE                    ... PORTS                  NAMES
------------ ------------------------     ---------------------- --------------------
abcCDEfghijk img-python-api-hello:1.0 ... 0.0.0.0:5050->4040/tcp cnt-python-api-hello
------------ ------------------------     ---------------------- --------------------
```
### :: Realizar pruebas hacia el servidor python local
```
> usando linea de comando:
$ curl http://localhost:5050/

> vía browser:
http://localhost:5050/

> resultado:
¡Hello world!
```
### :: Acceder por ssh al contenedor
```
$ docker exec -i -t cnt-python-api-hello /bin/sh

> resultado:
/app # ls
requirements.txt  server.py
/app # exit
```
### :: Revisar logs del servidor python
```
$ docker logs cnt-python-api-hello
```
### :: Detener el contenedor (esto lo elimina por tener la opción --rm al levantarlo)
```
docker stop cnt-python-api-hello
```