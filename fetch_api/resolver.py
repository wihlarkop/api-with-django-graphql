import graphene

from fetch_api.fetching import JsonPlaceHolderAPI

from fetch_api.schema import UserType, PostType

jph = JsonPlaceHolderAPI()


class JsonPlaceHolderQuery(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, user_id=graphene.ID())
    all_posts = graphene.List(PostType)
    post = graphene.Field(PostType, post_id=graphene.ID())

    def resolve_all_users(root, info):
        data = jph.fetch_all_users()
        return data

    def resolve_user(root, info, user_id: int):
        data = jph.fetch_user(user_id)
        return data

    def resolve_all_posts(root, info):
        data = jph.fetch_all_posts()
        return data

    def resolve_post(root, info, post_id: int):
        data = jph.fetch_post(post_id)
        return data

    def resolve_post_by_user(root, info, user_id: int):
        pass
