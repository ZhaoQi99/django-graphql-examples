import graphene
from graphene_django.types import DjangoObjectType

from account.models import User


class UserType(DjangoObjectType):
    today_join = graphene.Boolean()

    def resolve_today_join(self, info):
        return self.is_today_join()

    class Meta:
        model = User
        convert_choices_to_enum = False

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user_by_name = graphene.Field(UserType, user_name=graphene.String())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_user_by_name(self, info, user_name):
        return User.objects.filter(username=user_name).first()