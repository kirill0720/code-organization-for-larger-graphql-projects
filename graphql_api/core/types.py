import strawberry

from graphql_api.account import AccountQuery, AccountMutation
from graphql_api.product import ProductQuery, ProductMutation
from graphql_api.review import ReviewQuery, ReviewMutation
from graphql_api.checkout import CheckoutQuery, CheckoutMutation
from graphql_api.order import OrderQuery, OrderMutation
from graphql_api.shipping import ShippingQuery, ShippingMutation


@strawberry.type
class RootQuery(
    AccountQuery, ProductQuery, ReviewQuery, CheckoutQuery, OrderQuery, ShippingQuery
):
    pass


@strawberry.type
class RootMutation(
    AccountMutation,
    ProductMutation,
    ReviewMutation,
    CheckoutMutation,
    OrderMutation,
    ShippingMutation,
):
    pass
