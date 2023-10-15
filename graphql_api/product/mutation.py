import strawberry

from .types import Product, CreateProductInput


@strawberry.mutation
async def create_product(self, info, input: CreateProductInput) -> Product:
    # business logic on resolvers.py as resolve_create_product(info)
    return Product(title="Title", id=1)
