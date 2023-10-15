import strawberry

from .types import Product


@strawberry.field
def products(self, info) -> list[Product] | None:
    # business logic on resolvers.py as resolve_products(info)
    return [Product(title="Title", id=1)]


@strawberry.field
def product(self) -> Product | None:
    return Product(title="Title", id=1)
