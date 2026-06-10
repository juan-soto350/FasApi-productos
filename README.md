# Módulo 1 FastAPI Básico

## Descripción

Mini App desarrollada con FastAPI en Python para la gestión de un catálogo de productos usando API REST, la información se almacena en memoria de forma temporalmente y permite realizar operaciones CRUD (Crear, Consultar, Actualizar y Eliminar) que es lo pedido segun el intructor.

## Tecnologías utilizadas

* Python 3.13
* FastAPI
* Uvicorn[standar]
* Pydantic

## Instalación

1. Crear carpeta MODULO-1-FASTAPI-BASICO
2. Crear y activar un entorno virtual.
3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

## Acceso a la aplicación

API:

http://127.0.0.1:8000

Documentación:

http://127.0.0.1:8000/docs

## Endpoints disponibles

* GET /products
* GET /products/{product_id}
* POST /products
* PUT /products/{product_id}
* DELETE /products/{product_id}