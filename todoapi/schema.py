import graphene
from graphene_django import DjangoObjectType

from .models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'status')


class AddTodo(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    status = graphene.String()

    class Arguments:
        title = graphene.String()

    def mutate(root, info, title):
        todo = Todo(
            title=title
        )
        todo.save()

        return AddTodo(id=todo.id, title=todo.title, status=todo.status)


class TodoQuery(graphene.ObjectType):
    all_todos = graphene.List(TodoType)

    def resolve_all_todos(root, info):
        return Todo.objects.all()


class TodoMutation(graphene.ObjectType):
    add_todo = AddTodo.Field()
