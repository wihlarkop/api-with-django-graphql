from graphene import Date, Int, Mutation, ObjectType, String

from .models import DiaryPost


class AddDiary(Mutation):
    id = Int()
    timestamp = Date()
    post = String()

    class Arguments:
        timestamp = Date()
        post = String()

    @staticmethod
    def mutate(root, info, timestamp, post):
        diariespost = DiaryPost(
            timestamp=timestamp,
            post=post
        )
        diariespost.save()

        return AddDiary(id=diariespost.id, timestamp=diariespost.timestamp, post=diariespost.post)


class UpdateDiary(Mutation):
    id = Int()
    timestamp = Date()
    post = String()

    class Arguments:
        id = Int()
        timestamp = Date()
        post = String()

    @staticmethod
    def mutate(root, info, id, timestamp, post):
        diariespost = DiaryPost.objects.get(pk=id)
        diariespost.timestamp = timestamp
        diariespost.post = post
        diariespost.save()

        return UpdateDiary(id=diariespost.id, title=diariespost.timestamp, status=diariespost.post)


class DeleteDiary(Mutation):
    id = Int()

    class Arguments:
        id = Int()

    @staticmethod
    def mutate(root, info, id):
        diariespost = DiaryPost.objects.get(id=id)
        diariespost.delete()

        return None


class DiaryMutation(ObjectType):
    add_diary = AddDiary.Field()
    delete_diary = DeleteDiary.Field()
