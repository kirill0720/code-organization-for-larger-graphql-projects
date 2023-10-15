import strawberry

from graphql_api.account.types import Account, CreateAccountInput


@strawberry.type
class AccountMutation:
    @strawberry.mutation
    async def create_account(self, info, input: CreateAccountInput) -> Account:
        # business logic on resolvers.py as resolve_create_product(info)
        return Account(title="Title", id=1)
