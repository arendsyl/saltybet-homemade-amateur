from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

class PlayerRSA(Resource):

    def put(self, player: str)-> Dict[str, Any]:
        """
        Si le solde du joueur est strictement inférieur à 1000, set son solde à 1000.
        Erreur 404 si le joueur n'existe pas.
        200 si OK, 500 si erreur.
        ---
            tags:
                - Route pour les joueurs
            responses:
                - 200:
                    description: Le solde du joueur a bien été mis a jour
                - 404:
                    description: Le joueur n'existe pas
                - 500:
                    description: Erreur du serveur
        """
        return {"message":f"PUT players/{player}/rsa"}, 200
