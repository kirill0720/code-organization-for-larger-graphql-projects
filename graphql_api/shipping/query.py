import typing

import strawberry

from .types import Shipping


@strawberry.type
class ShippingQuery:
    @strawberry.field
    def shippings(self, info) -> typing.Optional[typing.List[Shipping]]:
        # business logic on resolvers.py as resolve_shippings(info)
        return [Shipping(title="Title", id=1)]

    @strawberry.field
    def shipping(self) -> typing.Optional[Shipping]:
        return Shipping(title="Title", id=1)
