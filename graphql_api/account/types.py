import typing

import strawberry


@strawberry.type
class Account:
    title: str
    id: typing.Optional[strawberry.ID] = None


@strawberry.input
class CreateAccountInput:
    title: str


@strawberry.input
class CreateAccount:
    input: CreateAccountInput
