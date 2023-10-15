import typing

import strawberry


@strawberry.type
class Checkout:
    title: str
    id: typing.Optional[strawberry.ID] = None


@strawberry.input
class CreateCheckoutInput:
    title: str


@strawberry.input
class CreateCheckout:
    input: CreateCheckoutInput
