import pymysql
from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask import Blueprint

pymysql.install_as_MySQLdb()

# app initialization
app = Flask(__name__)
CORS(app)

api = Api(app)

# Imports
import os
from graph_ql import schema
from flask_graphql import GraphQLView
from application import app, api
from api.user import ns as user
from api.post import ns as post

app.debug = True

# Routes
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

api.add_namespace(user)
api.add_namespace(post)


if __name__ == '__main__':
    app.run()
