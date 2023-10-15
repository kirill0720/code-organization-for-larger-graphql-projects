import typing

import strawberry


@strawberry.type
class Shipping:
    title: str
    id: typing.Optional[strawberry.ID] = None


@strawberry.input
class CreateShippingInput:
    title: str


@strawberry.input
class CreateShipping:
    input: CreateShippingInput
