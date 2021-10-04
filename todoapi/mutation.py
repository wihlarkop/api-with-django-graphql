from graphene import Int, Mutation, ObjectType, String

from .models import Todo
from .schema import StatusEnum


class AddTodo(Mutation):
    id = Int()
    title = String()
    status = String()

    class Arguments:
        title = String()

    @staticmethod
    def mutate(root, info, title):
        todo = Todo(
            title=title
        )
        todo.save()

        return AddTodo(id=todo.id, title=todo.title, status=todo.status)


class UpdateStatusTodo(Mutation):
    id = Int()
    title = String()
    status = String()

    class Arguments:
        id = Int()
        status = StatusEnum()

    @staticmethod
    def mutate(root, info, id, status):
        todo = Todo.objects.get(pk=id)
        todo.status = status
        todo.save()

        return UpdateStatusTodo(id=todo.id, title=todo.title, status=todo.status)


class DeleteTodo(Mutation):
    id = Int()

    class Arguments:
        id = Int()

    @staticmethod
    def mutate(root, info, id):
        todo = Todo.objects.get(id=id)
        todo.delete()

        return None


class TodoMutation(ObjectType):
    add_todo = AddTodo.Field()
    update_status_todo = UpdateStatusTodo.Field()
    delete_todo = DeleteTodo.Field()
