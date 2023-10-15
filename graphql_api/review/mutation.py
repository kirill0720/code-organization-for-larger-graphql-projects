import strawberry

from .types import Review, CreateReviewInput


@strawberry.type
class ReviewMutation:
    @strawberry.mutation
    async def create_review(self, info, input: CreateReviewInput) -> Review:
        # business logic on resolvers.py as resolve_create_review(info)
        return Review(title="Title", id=1)
