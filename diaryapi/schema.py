import graphene
from graphene_django import DjangoObjectType

from .models import DiaryPost


class DiaryPostType(DjangoObjectType):
    class Meta:
        model = DiaryPost
        fields = ()


class DiaryQuery(graphene.ObjectType):
    all_diaries = graphene.List(DiaryPostType)

    @staticmethod
    def resolve_all_diaries(root, info):
        return DiaryPost.objects.all()


class DiaryMutation(graphene.ObjectType):
    pass
