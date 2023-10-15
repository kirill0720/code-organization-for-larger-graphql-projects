import strawberry

from .types import Shipping, CreateShippingInput


@strawberry.mutation
async def create_shipping(self, info, input: CreateShippingInput) -> Shipping:
    # business logic on resolvers.py as resolve_create_shipping(info)
    return Shipping(title="Title", id=1)
