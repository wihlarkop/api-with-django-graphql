from graphene import Field, Int, List, ObjectType

from .models import DiaryPost
from .schema import DiaryPostType


class DiaryQuery(ObjectType):
    all_diaries = List(DiaryPostType)
    diary = Field(DiaryPostType, diary_id=Int())

    @staticmethod
    def resolve_all_diaries(root, info):
        return DiaryPost.objects.all()

    @staticmethod
    def resolve_diary(root, info, diary_id):
        return DiaryPost.objects.get(id=diary_id)
