import graphene

from diaryapi.resolver import DiaryQuery
from diaryapi.mutation import DiaryMutation
from fetch_api.resolver import JsonPlaceHolderQuery
from todoapi.mutation import TodoMutation
from todoapi.resolver import TodoQuery


class Query(DiaryQuery, TodoQuery, JsonPlaceHolderQuery, graphene.ObjectType):
    pass


class Mutation(DiaryMutation, TodoMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
