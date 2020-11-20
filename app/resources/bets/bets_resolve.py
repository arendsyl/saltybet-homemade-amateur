from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any, Tuple


class BetsResolve(Resource):

    def post(self, champion) -> Tuple[Dict[str, Any], int]:
        """
        `champion` est un `int` dont la valeur est 1 ou 2. Résout tous les \
            bets en cours et incrémente les soldes des joueurs au besoin. Dump \
                l'état de la collection `players` dans la collection \
                    `ongoing_bets` de manière horodatée.
        ---
        tags:
            - Routes du MJ
        parameters:
            - in: body
              name: auth_token
              description: Token d'authentification du MJ
              required: true
              type: string
            - in: path
              name: champion
              description: 1 pour le Player 1 ou 2 pour le Player 2
              required: true
              type: int
        responses:
            200:
                description: La base a correctement été réinitialisée
            403:
                description: Authentification incorrecte ou bets encore ouverts
            500:
                description: Erreur interne du serveur
        """

        try:
            # TODO : Implémentation
            return {"message": "Valeur du bet multipler modifiée"}, 200
        except Exception:
            return {"message": "Erreur interne du serveur"}, 500
