import graphene

from .models import DiaryPost
from .schema import DiaryPostType


class DiaryQuery(graphene.ObjectType):
    all_diaries = graphene.List(DiaryPostType)
    diary = graphene.Field(DiaryPostType, diary_id=graphene.Int())

    @staticmethod
    def resolve_all_diaries(root, info):
        return DiaryPost.objects.all()

    @staticmethod
    def resolve_diary(root, info, diary_id):
        return DiaryPost.objects.get(id=diary_id)
