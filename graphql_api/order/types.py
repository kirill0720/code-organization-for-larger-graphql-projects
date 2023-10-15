import typing

import strawberry


@strawberry.type
class Order:
    title: str
    id: typing.Optional[strawberry.ID] = None


@strawberry.input
class CreateOrderInput:
    title: str


@strawberry.input
class CreateOrder:
    input: CreateOrderInput
