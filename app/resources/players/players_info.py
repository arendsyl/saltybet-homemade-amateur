from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

class PlayersInfo(Resource):
    
    def get(self) -> Dict[str, Any]:
        """
        Retourne un dictionnaire avec la liste des joueurs présents et leur solde.
        200 si OK, 500 si erreur.
        ---
            tags: 
                - Route pour les joueurs
            responses:
                - 200:
                    description: Renvoie la liste des joueurs
                - 500:
                    description: Erreur du serveur
        """
        return {"message":"GET players"}, 200
