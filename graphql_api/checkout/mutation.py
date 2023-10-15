import strawberry

from .types import Checkout, CreateCheckoutInput


@strawberry.type
class CheckoutMutation:
    @strawberry.mutation
    async def create_checkout(self, info, input: CreateCheckoutInput) -> Checkout:
        # business logic on resolvers.py as resolve_create_checkout(info)
        return Checkout(title="Title", id=1)
