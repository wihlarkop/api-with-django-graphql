from graphene import List, ObjectType

from .models import Todo
from .schema import TodoType


class TodoQuery(ObjectType):
    all_todos = List(TodoType)

    @staticmethod
    def resolve_all_todos(root, info):
        return Todo.objects.all()
