import graphene

from .models import DiaryPost


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


class DiaryMutation(graphene.ObjectType):
    add_diary = AddDiary.Field()
    update_diary = UpdateDiary.Field()
    delete_diary = DeleteDiary.Field()
