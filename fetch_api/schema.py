import graphene


class TodoType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    completed = graphene.Boolean()


class PostType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    body = graphene.String()
    userId = graphene.ID()


class UserCompanyType(graphene.ObjectType):
    name = graphene.String()
    catchPhrase = graphene.String()
    bs = graphene.String()


class UserAddressGeoLocationType(graphene.ObjectType):
    lat = graphene.String()
    lng = graphene.String()


class UserAddressType(graphene.ObjectType):
    street = graphene.String()
    suite = graphene.String()
    city = graphene.String()
    zipcode = graphene.String()
    geo = graphene.Field(UserAddressGeoLocationType)


class UserType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    username = graphene.String()
    email = graphene.String()
    address = graphene.Field(UserAddressType)
    phone = graphene.String()
    website = graphene.String()
    company = graphene.Field(UserCompanyType)
    posts = graphene.List(PostType)
    todos = graphene.List(TodoType)
