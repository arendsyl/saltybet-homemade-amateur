from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any, Tuple


class Init(Resource):

    def post(self) -> Tuple[Dict[str, Any], int]:
        """
        Purge l'intégralité de la base et réinitialise complètement la base (joueurs et bets). A utiliser avec modération.
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
            return {"message": "Serveur de bets réinitialisé !"}, 200
        except Exception:
            return {"message": "Erreur interne du serveur"}, 500
