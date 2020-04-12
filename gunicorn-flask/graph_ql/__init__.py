# Imports
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graph_ql.schema import PostObject, UserObject
from graph_ql.user import CreateUser, DeleteUser
from graph_ql.post import CreatePost, DeletePost
from db_models.models import User


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    delete_post = DeletePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


