import graphene

from fetch_api.fetching import JsonPlaceHolderAPI
from fetch_api.schema import UserType, PostType, TodoType

jph = JsonPlaceHolderAPI()


class JsonPlaceHolderQuery(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, user_id=graphene.ID())

    all_posts = graphene.List(PostType)
    post = graphene.Field(PostType, post_id=graphene.ID())
    posts_by_user_id = graphene.List(PostType, user_id=graphene.ID())

    all_todos = graphene.List(TodoType)
    todo = graphene.Field(TodoType, todo_id=graphene.ID())
    todos_by_user_id = graphene.List(TodoType, user_id=graphene.ID())

    def resolve_all_users(root, info):
        users = jph.fetch_all_users()
        return users

    def resolve_user(root, info, user_id: int):
        user = jph.fetch_user(user_id=user_id)
        # user['posts'] = jph.fetch_posts_by_user_id(user_id=user_id)
        # user['todos'] = jph.fetch_todo_by_user_id(user_id=user_id)
        return user

    def resolve_all_posts(root, info):
        posts = jph.fetch_all_posts()
        return posts

    def resolve_post(root, info, post_id: int):
        post = jph.fetch_post(post_id=post_id)
        return post

    def resolve_posts_by_user_id(root, info, user_id: int):
        posts = jph.fetch_posts_by_user_id(user_id=user_id)
        return posts

    def resolve_all_todos(root, info):
        todos = jph.fetch_all_todos()
        return todos

    def resolve_todo(root, info, todo_id: int):
        todo = jph.fetch_todo(todo_id=todo_id)
        return todo

    def resolve_todos_by_user_id(root, info, user_id: int):
        posts = jph.fetch_todo_by_user_id(user_id=user_id)
        return posts
