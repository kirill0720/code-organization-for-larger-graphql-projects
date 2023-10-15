import typing

import strawberry

from .types import Order


@strawberry.type
class OrderQuery:
    @strawberry.field
    def orders(self, info) -> typing.Optional[typing.List[Order]]:
        # business logic on resolvers.py as resolve_orders(info)
        return [Order(title="Title", id=1)]

    @strawberry.field
    def order(self) -> typing.Optional[Order]:
        return Order(title="Title", id=1)
