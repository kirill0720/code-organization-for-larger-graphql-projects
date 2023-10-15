import strawberry

from .types import Order, CreateOrderInput


@strawberry.mutation
async def create_order(self, info, input: CreateOrderInput) -> Order:
    # business logic on resolvers.py as resolve_create_order(info)
    return Order(title="Title", id=1)
