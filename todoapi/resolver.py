import graphene

from .models import Todo
from .schema import TodoType


class TodoQuery(graphene.ObjectType):
    all_todos = graphene.List(TodoType)

    @staticmethod
    def resolve_all_todos(root, info):
        return Todo.objects.all()
