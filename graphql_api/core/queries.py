from strawberry.tools import create_type

from graphql_api.account.query import accounts, account
from graphql_api.checkout.query import checkouts, checkout
from graphql_api.order.query import orders, order
from graphql_api.product.query import products, product
from graphql_api.review.query import reviews, review
from graphql_api.shipping.query import shippings, shipping

Query = create_type(
    "Query",
    [
        accounts,
        account,
        products,
        product,
        reviews,
        review,
        checkouts,
        checkout,
        orders,
        order,
        shippings,
        shipping,
    ]
)
