import typing

import strawberry


@strawberry.type
class Product:
    title: str
    id: typing.Optional[strawberry.ID] = None


@strawberry.input
class CreateProductInput:
    title: str


@strawberry.input
class CreateProduct:
    input: CreateProductInput
