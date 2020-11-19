from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

from app.features.shape import dataframe_shape


class DataFrameShape(Resource):

    def post(self) -> Dict[str, Any]:
        """
        Retourne la forme du dataset compris dans l'url passée dans \
            le body de la requête http
        ---
        tags:
            - POC Flask API
        parameters:
            - in: body
              name: url
              description: URL qui pointe vers un .CSV
              required: true
              type: string
        responses:
            200:
                description: Json contenant la forme du dataframe passé dans le body de la requête HTTP.
            404:
                description: La valeur de la clé dans le body de la requête n'est pas 'url'
        """

        body_parser = reqparse.RequestParser()
        body_parser.add_argument('url')
        args = body_parser.parse_args()
        try:
            url = args['url']
            return dataframe_shape(url), 200
        except Exception:  # TODO spécifiez plus spécifiquement l'exception
            return {"message": "Error, URL not found"}, 404

    def get(self) -> Dict[str, Any]:
        """
        Retourne la forme du dataset compris dans le paramètre 'url'
            passé dans l'URL
        ---
        tags:
            - POC Flask API
        parameters:
            - in: URL
              name: url
              description: URL qui pointe vers un .CSV
              required: true
              type: string
        responses:
            200:
                description: Json contenant la forme du dataframe passé dans le body de la requête HTTP.
            404:
                description: La valeur de la clé dans le body de la requête n'est pas 'url'
        """
        url_args = request.args
        try:
            url = url_args['url']
            return dataframe_shape(url), 200
        except Exception:
            return {"message": "Error, URL not found"}, 404
