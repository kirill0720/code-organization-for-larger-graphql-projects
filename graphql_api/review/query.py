import strawberry

from .types import Review


@strawberry.field
def reviews(self, info) -> list[Review] | None:
    # business logic on resolvers.py as resolve_reviews(info)
    return [Review(title="Title", id=1)]


@strawberry.field
def review(self) -> Review | None:
    return Review(title="Title", id=1)
