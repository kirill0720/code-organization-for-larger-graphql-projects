from strawberry.tools import create_type

from graphql_api.account.mutation import create_account
from graphql_api.checkout.mutation import create_checkout
from graphql_api.order.mutation import create_order
from graphql_api.product.mutation import create_product
from graphql_api.review.mutation import create_review
from graphql_api.shipping.mutation import create_shipping

Mutation = create_type(
    "Mutation",
    [
        create_account,
        create_checkout,
        create_product,
        create_review,
        create_shipping,
        create_order,
    ]
)
