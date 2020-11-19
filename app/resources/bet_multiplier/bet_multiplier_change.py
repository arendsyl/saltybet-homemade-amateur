from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any, Tuple


class BetMultiplierChange(Resource):

    def put(self, facteur) -> Tuple[Dict[str, Any], int]:
        """
        `facteur` est un `float`. Modifie la valeur de `BET_MULTIPLIER`. La \
            valeur doit être comprise entre 1 et 5.
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
            return {"message": "Valeur du bet multipler modifiée"}, 200
        except Exception:
            return {"message": "Erreur interne du serveur"}, 500
