from django import forms
import graphene
from graphene_django import DjangoListField
from graphene_django.types import DjangoObjectType

from account.models import Token, User


class UserType(DjangoObjectType):
    today_join = graphene.Boolean()

    def resolve_today_join(self, info):
        return self.is_today_join()

    @classmethod
    def get_queryset(cls, queryset, info):
      return queryset.exclude(username='admin')

    class Meta:
        model = User
        convert_choices_to_enum = False

class UserQuery(graphene.ObjectType):
    users = DjangoListField(UserType)
    user_by_name = graphene.Field(UserType, user_name=graphene.String())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_user_by_name(self, info, user_name):
        return User.objects.filter(username=user_name).first()


class TokenType(DjangoObjectType):
    class Meta:
        model = Token

class TokenQuery(graphene.ObjectType):
    token_by_value = graphene.Field(TokenType, value=graphene.String())

    def resolve_token_by_value(self, info, value):
        return Token.objects.filter(token=value).first()


class UserMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self,info, user_name, password, email):
        user = User.objects.create_user(user_name, email, password)
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    create_user = UserMutation.Field()

class Query(UserQuery,TokenQuery):
    pass
