import graphene
from graphene_django.debug import DjangoDebug
import account.schema


class Query(account.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')



class Mutation(account.schema.Mutation, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')

schema = graphene.Schema(query=Query, mutation=Mutation)