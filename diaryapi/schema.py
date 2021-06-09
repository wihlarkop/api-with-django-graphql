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
        diariespost = DiaryPost(
            timestamp=timestamp,
            post=post
        )
        diariespost.save()

        return AddDiary(id=diariespost.id, timestamp=diariespost.timestamp, post=diariespost.post)


class UpdateDiary(graphene.Mutation):
    id = graphene.Int()
    timestamp = graphene.Date()
    post = graphene.String()

    class Arguments:
        id = graphene.Int()
        timestamp = graphene.Date()
        post = graphene.String()

    @staticmethod
    def mutate(root, info, id, timestamp, post):
        diariespost = DiaryPost.objects.get(pk=id)
        diariespost.timestamp = timestamp
        diariespost.post = post
        diariespost.save()

        return UpdateDiary(id=diariespost.id, title=diariespost.timestamp, status=diariespost.post)


class DeleteDiary(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    @staticmethod
    def mutate(root, info, id):
        diariespost = DiaryPost.objects.get(id=id)
        diariespost.delete()

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
