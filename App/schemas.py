from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    price: float = Field(..., ge=0)
    stock: int = Field(..., ge=0)


class ProductResponse(Product):
    id: int


class ProductUpdate(Product):
    pass