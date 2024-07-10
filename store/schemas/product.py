from typing import Optional
from pydantic import BaseModel, Field

from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product Name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    ...


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(description="Product quantity")
    price: Optional[float] = Field(description="Product price")
    status: Optional[bool] = Field(description="Product status")


class ProductUpdateOut(ProductUpdate):
    ...
