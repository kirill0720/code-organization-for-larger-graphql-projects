import typing

import strawberry

from .types import Checkout


@strawberry.type
class CheckoutQuery:
    @strawberry.field
    def checkouts(self, info) -> typing.Optional[typing.List[Checkout]]:
        # business logic on resolvers.py as resolve_checkouts(info)
        return [Checkout(title="Title", id=1)]

    @strawberry.field
    def checkout(self) -> typing.Optional[Checkout]:
        return Checkout(title="Title", id=1)
