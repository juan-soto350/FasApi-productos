from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

class ProductUpdate(ProductCreate):
    id: int

class ProductResponse(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
