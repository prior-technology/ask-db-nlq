import graphene
from flask_graphql import GraphQLView
from flask import Flask
from schema import build_schema
import apprun
#import engine
import os

model_dir = os.getenv('MODEL_DIR', '/data_model/wikisql')
data_dir = os.getenv('DATA_DIR', model_dir + '/data')

(rootQueryClass,mutationsClass) = build_schema(data_dir)
schema = graphene.Schema(query=rootQueryClass, mutation=mutationsClass)

app = Flask(__name__)

#(translator, opt) = apprun.initialise(app)

@app.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers']= 'Origin, X-Requested-With, Content-Type, Accept'
    return response

@app.route('/ping')
def ping():
    return "pong"


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

#engine.init(model_dir)

# Optional, for adding batch query support (used in Apollo-Client)
#app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))
