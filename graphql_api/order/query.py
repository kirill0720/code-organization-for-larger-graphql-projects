import strawberry

from .types import Order


@strawberry.field
def orders(self, info) -> list[Order] | None:
    # business logic on resolvers.py as resolve_orders(info)
    return [Order(title="Title", id=1)]


@strawberry.field
def order(self) -> Order | None:
    return Order(title="Title", id=1)
