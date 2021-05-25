import graphene

from todoapi.schema import TodoQuery, TodoMutation


class Query(TodoQuery, graphene.ObjectType):
    pass


class Mutation(TodoMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
