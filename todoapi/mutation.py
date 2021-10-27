import graphene

from .models import Todo
from .schema import StatusEnum


class AddTodo(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    status = graphene.String()

    class Arguments:
        title = graphene.String()

    @staticmethod
    def mutate(root, info, title):
        todo = Todo(
            title=title
        )
        todo.save()

        return AddTodo(id=todo.id, title=todo.title, status=todo.status)


class UpdateStatusTodo(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    status = graphene.String()

    class Arguments:
        id = graphene.Int()
        status = StatusEnum()

    @staticmethod
    def mutate(root, info, id, status):
        todo = Todo.objects.get(pk=id)
        todo.status = status
        todo.save()

        return UpdateStatusTodo(id=todo.id, title=todo.title, status=todo.status)


class DeleteTodo(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    @staticmethod
    def mutate(root, info, id):
        todo = Todo.objects.get(id=id)
        todo.delete()

        return None


class TodoMutation(graphene.ObjectType):
    add_todo = AddTodo.Field()
    update_status_todo = UpdateStatusTodo.Field()
    delete_todo = DeleteTodo.Field()
