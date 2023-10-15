from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from graphql_api.core.schema import schema


def create_app() -> FastAPI:
    app = FastAPI()
    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")

    @app.get("/")
    async def root():
        return {"message": "For GraphQL go to /graphql"}

    return app
