import graphene
from graphql_auth.schema import UserQuery, MeQuery

# user query for graphql is coming from here through graphql
class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)