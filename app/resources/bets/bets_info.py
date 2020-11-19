from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any


class BetsInfo(Resource):

    def get(self) -> Dict[str, Any]:
        """
        Retourne un dictionnaire sous cette forme :
        ```javascript
        {
            "1": [
                {"nom_joueur": 200}
                // Liste des bets sur le PLAYER 1
            ],
            "2": [
                {"nom_joueur_b": 200}
                // Liste des bets sur le PLAYER 2
            ]
        }
        ```
        ---
            tags: 
                - Route pour les joueurs
            responses:
                - 200:
                    description: Renvoie la liste des paris en cours
                - 500:
                    description: erreur du serveur
        """
        return {"message": "GET bets"}, 200
