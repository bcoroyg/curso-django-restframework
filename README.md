# CURSO DJANGO REST FRAMEWORK

## Arquitectura de una aplicacion

### Backend
- Consiste en:
* Servidor
* Aplicacion
* Base de Datos

### Arquitectura
* Monolitica
* Distribuida
* Hibrida
* Orientada a Servicios (SOA)

### Arquitectura Orientada a Servicios (SOA)
* Es auto-contenida.
* Es una caja negra para sus consumidores
* Representa una actividad de negocio con un fin especifico

### Web Services
- Es la forma en la que se implementa las arquirecturas a servicios
* SOAP - XML
* RESTful HTTP - JSON
* GraphQL

### CODEBASE
- **Objetivos:**
* Configuracion declarativa.
* Contrato claro con el OS.
* Lista para lanzar.
* Reducir diferencia entre entornos.
* Facil de escalar.



### DOCKER
* No necesita un "Guest OS".
* Usa muy poca memoria.
* Facil de replicar y controlar.
* Facil de compartir.

- Django: 8000
- PostgreSQL: 5432
- Redis: 6379
- Celery(Flower): 5555

* Construir las imagenes del proyecto.
```
docker compose -f local.yml build
```

* Correr el stack.
```
docker compose -f local.yml up
```

#########################
         ERROR
#########################
* AttributeError: module 'tornado.web' has no attribute 'asynchronous'

#########################
        SOLUCION
#########################
* En requirements base.py agregar la siguiente dependencia.
```
tornado>=5.0.0,<6.0.0
```

* Listar imagenes que estan corriendo.
```
docker compose -f local.yml ps
```

* Bajar todos los servicios.
```
docker compose -f local.yml down
```

### Prop tip
```
export COMPOSE_FILE='local.yml'
docker compose build
docker compose up
docker compose ps
docker compose down

```

### Comandos de Administración
```
docker compose run --rm django COMMAND
```

```
docker compose run --rm django \
        python manage.py createsuperuser
```

### Habilitar Debuger
```
docker compose up
docker compose ps
docker rm -f <ID>
```
* Nota: Bajar contenedor Django.
```
docker compose run --rm --service-ports django
```

### Mas comandos de docker
```
docker compose images

docker container
docker images
docker volume
docker network
```

* ls
* rm
* prune
* -a
* -q

### MIGRACIONES
```
docker compose run --rm django python manage.py makemigrations    
```

## COOKIECUTTER
* [Link](https://cookiecutter.readthedocs.io/en/stable/)

## SHELL PLUS DJANGO
```
docker compose -f local.yml run --rm django python manage.py shell_plus
```

## INSTALACION DE HTTPIE
```
pip install httpie 
```

### USO DE HTTPIE
```
http localhost:8000/circles

http localhost:8000/circles -b

http localhost:8000/circles -v

```
