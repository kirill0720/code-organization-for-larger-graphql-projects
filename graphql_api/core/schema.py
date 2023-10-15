import strawberry

from graphql_api.core.mutations import Mutation
from graphql_api.core.queries import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
