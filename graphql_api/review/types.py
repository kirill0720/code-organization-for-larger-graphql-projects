import typing

import strawberry


@strawberry.type
class Review:
    title: str
    id: typing.Optional[strawberry.ID] = None


@strawberry.input
class CreateReviewInput:
    title: str


@strawberry.input
class CreateReview:
    input: CreateReviewInput
