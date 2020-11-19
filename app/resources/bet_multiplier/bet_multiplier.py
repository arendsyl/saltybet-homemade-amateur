from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

class BetMultiplierInfo(Resource):

    def get(self) -> Dict[str, Any]:
        """
        Retourne la valeur de `BET_MULTIPLIER` 200 si OK, 500 si erreur.
        ---
            tags: 
                - Route pour les joueurs
            responses:
                - 200:
                    description: La valeur de `BET_MULTIPLIER` est bien renvoyée
                - 500:
                    description: Erreur pour récupérer la valeur de `BET_MULTIPLIER` dans la base
        """
        try:
            
            return {"message": "GET bet_multiplier"}, 200
        except Exception:
            return {"message": "Erreur interne du serveur"}, 500
        
