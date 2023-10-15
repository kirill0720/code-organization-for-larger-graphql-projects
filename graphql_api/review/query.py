import typing

import strawberry

from .types import Review


@strawberry.type
class ReviewQuery:
    @strawberry.field
    def reviews(self, info) -> typing.Optional[typing.List[Review]]:
        # business logic on resolvers.py as resolve_reviews(info)
        return [Review(title="Title", id=1)]

    @strawberry.field
    def review(self) -> typing.Optional[Review]:
        return Review(title="Title", id=1)
