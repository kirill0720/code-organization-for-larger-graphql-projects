import strawberry

from .types import Checkout


@strawberry.field
def checkouts(self, info) -> list[Checkout] | None:
    # business logic on resolvers.py as resolve_checkouts(info)
    return [Checkout(title="Title", id=1)]


@strawberry.field
def checkout(self) -> Checkout | None:
    return Checkout(title="Title", id=1)
