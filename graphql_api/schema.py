import strawberry

from graphql_api.core.types import RootQuery#, RootMutation
from graphql_api.core.mutations import Mutation


@strawberry.type
class Query(RootQuery):
    pass


# @strawberry.type
# class Mutation(RootMutation):
#     pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
