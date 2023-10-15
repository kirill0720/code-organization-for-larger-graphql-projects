import typing

import strawberry

from .types import Product


@strawberry.type
class ProductQuery:
    @strawberry.field
    def products(self, info) -> typing.Optional[typing.List[Product]]:
        # business logic on resolvers.py as resolve_products(info)
        return [Product(title="Title", id=1)]

    @strawberry.field
    def product(self) -> typing.Optional[Product]:
        return Product(title="Title", id=1)
