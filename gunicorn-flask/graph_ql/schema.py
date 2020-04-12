# Imports
from graphene_sqlalchemy import SQLAlchemyObjectType
from db_models.models import User, Post
import graphene


class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node, )


class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = User
       interfaces = (graphene.relay.Node, )
