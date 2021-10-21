from graphene_django import DjangoObjectType

from .models import DiaryPost


class DiaryPostType(DjangoObjectType):
    class Meta:
        model = DiaryPost
        fields = ('id', 'timestamp', 'post')
