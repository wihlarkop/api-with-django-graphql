import graphene
from todoapi.schema import TodoQuery


class Query(TodoQuery, graphene.ObjectType):
    pass


# class Mutation(graphene.Mutation):
#     pass


schema = graphene.Schema(query=Query)
