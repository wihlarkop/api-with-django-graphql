import graphene

from diaryapi.schema import DiaryQuery, DiaryMutation
from todoapi.schema import TodoQuery, TodoMutation


class Query(DiaryQuery, TodoQuery, graphene.ObjectType):
    pass


class Mutation(DiaryMutation, TodoMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
