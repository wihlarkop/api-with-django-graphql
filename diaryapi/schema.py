import graphene
from graphene_django import DjangoObjectType

from .models import DiaryPost


class DiaryPostType(DjangoObjectType):
    class Meta:
        model = DiaryPost
        fields = ('id', 'timestamp', 'post')


class AddDiary(graphene.Mutation):
    id = graphene.Int()
    timestamp = graphene.Date()
    post = graphene.String()

    class Arguments:
        timestamp = graphene.Date()
        post = graphene.String()

    @staticmethod
    def mutate(root, info, timestamp, post):
        post = DiaryPost(
            timestamp=timestamp,
            post=post
        )
        post.save()

        return AddDiary(id=post.id, timestamp=post.timestamp, post=post.post)


class DeleteDiary(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    @staticmethod
    def mutate(root, info, id):
        post = DiaryPost.objects.get(id=id)
        post.delete()

        return None


class DiaryQuery(graphene.ObjectType):
    all_diaries = graphene.List(DiaryPostType)
    diary = graphene.Field(DiaryPostType, diary_id=graphene.Int())

    @staticmethod
    def resolve_all_diaries(root, info):
        return DiaryPost.objects.all()

    @staticmethod
    def resolve_diary(root, info, diary_id):
        return DiaryPost.objects.get(id=diary_id)


class DiaryMutation(graphene.ObjectType):
    add_diary = AddDiary.Field()
    delete_diary = DeleteDiary.Field()
