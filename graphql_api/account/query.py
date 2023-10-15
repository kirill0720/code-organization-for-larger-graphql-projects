import strawberry

from graphql_api.account.types import Account


@strawberry.type
class AccountQuery:
    @strawberry.field
    def accounts(self, info) -> list[Account] | None:
        # business logic on resolvers.py as resolve_products(info)
        return [Account(title="Title", id=1)]

    @strawberry.field
    def account(self) -> Account | None:
        return Account(title="Title", id=1)
