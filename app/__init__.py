# Flask import
from flask import Flask, jsonify
from flask_restful import Api, reqparse
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

# Creating the app
app = Flask(__name__)
CORS(app)
api = Api(app)

# Import configuration and routes
from app import config  # nopep8
from app import routes  # nopep8

# Definition de l'environnement de configuration
if config.ENVIRONMENT == 'prod':
    conf = config.ProductionConfig
else:
    conf = config.DevelopmentConfig

# Setup the right Flask config
app.config.from_object(conf)

# Create the route where SWAGGER can get the API documentation
@app.route('/spec')
def spec():
    swag = swagger(app)
    swag['info']['version'] = config.VERSION
    swag['info']['title'] = config.API_NAME
    return jsonify(swag)


# Get the values to set SWAGGER at the right place on the server
swaggerui_blueprint = get_swaggerui_blueprint(
    conf.SWAGGER_URL,
    conf.API_URL,
    config={
        'app_name': conf.API_NAME
    }
)

# Apply these values to the Flask app which is an API
app.register_blueprint(swaggerui_blueprint, url_prefix=conf.SWAGGER_URL)
