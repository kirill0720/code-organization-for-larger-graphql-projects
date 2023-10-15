import strawberry

from .types import Shipping


@strawberry.field
def shippings(self, info) -> list[Shipping] | None:
    # business logic on resolvers.py as resolve_shippings(info)
    return [Shipping(title="Title", id=1)]


@strawberry.field
def shipping(self) -> Shipping | None:
    return Shipping(title="Title", id=1)
