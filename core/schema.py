import graphene

from diaryapi.schema import DiaryQuery, DiaryMutation
from todoapi.mutation import TodoMutation
from todoapi.resolver import TodoQuery


class Query(DiaryQuery, TodoQuery, graphene.ObjectType):
    pass


class Mutation(DiaryMutation, TodoMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
