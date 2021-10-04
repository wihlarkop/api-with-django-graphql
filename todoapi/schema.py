from graphene import Enum
from graphene_django import DjangoObjectType

from .models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'status')


class StatusEnum(Enum):
    DONE = 'Done'
    ON_PROCESS = 'On Process'


