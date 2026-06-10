from fastapi import FastAPI, HTTPException
from App.schemas import ProductCreate, ProductResponse, ProductUpdate

app = FastAPI()

products = []
next_id = 1


@app.get("/")
def root():
    return {"message": "API de Productos funcionando"}


@app.get("/products")
def get_products(min_stock: int = 0):
    return [p for p in products if p["stock"] >= min_stock]


@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):

    global next_id

    new_product = {
        "id": next_id,
        "name": product.name,
        "price": product.price,
        "stock": product.stock
    }

    products.append(new_product)
    next_id += 1

    return new_product


@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate
):

    for p in products:

        if p["id"] == product_id:

            p["name"] = product.name
            p["price"] = product.price
            p["stock"] = product.stock

            return p

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):

    for index, product in enumerate(products):

        if product["id"] == product_id:
            products.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )