from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any, Tuple


class BetsClose(Resource):

    def put(self) -> Tuple[Dict[str, Any], int]:
        """
        Ne fait rien si `BETS_OPEN` est `False`. Passe `BETS_OPEN` à False.
        ---
        tags:
            - Routes du MJ
        parameters:
            - in: body
              name: auth_token
              description: Token d'authentification du MJ
              required: true
              type: string
        responses:
            200:
                description: La base a correctement été réinitialisée
            403:
                description: Authentification incorrecte
            500:
                description: Erreur interne du serveur
        """

        try:
            # TODO : Implémentation
            return {"message": "Les paris sont fermés !"}, 200
        except Exception:
            return {"message": "Erreur interne du serveur"}, 500
