from strawberry.tools import create_type

from graphql_api.account.query import account
from graphql_api.checkout.query import checkout
from graphql_api.order.query import order
from graphql_api.product.query import product
from graphql_api.review.query import review
from graphql_api.shipping.query import shipping

Mutation = create_type(
    "Query",
    [
        create_account,
        create_checkout,
        create_product,
        create_review,
        create_shipping,
        create_order,
    ]
)
