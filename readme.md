# Python/Flask - API Hello
Esta es una simple API construida con el lenguaje de programación Python y su framework Flask, con la finalidad de ser levantada en un contenedor docker local, para terminar siendo subida al docker hub público.
### :: Clonar repositorio
```
clone https://github.com/galvarezdevs/python-api-hello.git
```
### :: Crear imagen python con framework flash
```
docker build -t img-python-api-hello:1.0 -f docker/dockerfile.dev .
```
### :: Levantar contenedor con la imagen python
```
docker run -i -t -d --rm -v ${PWD}/src:/app -p 5050:4040 --name cnt-python-api-hello img-python-api-hello:1.0
```
### :: Acceder por ssh al contenedor
```
docker exec -i -t cnt-python-api-hello /bin/sh
```
### :: Revisar logs del servidor python
```
docker logs cnt-python-api-hello
```
### :: Detener el contenedor (esto lo elimina por tener la opción --rm al levantarlo)
```
docker stop cnt-python-api-hello
```
