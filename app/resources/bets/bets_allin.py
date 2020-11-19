from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

from app.features.ia_champion import ChampionEnum

class BetsAllIn(Resource):
    def post(self, player: str, ia_champion: int) -> Dict[str, Any]:
        """
        Le joueur `player` (str) mise tout son solde sur le `ia_champion` (int mais valeurs uniquement possibles : 1 ou 2).
        ---
            tags: 
                - Route pour les joueurs
            responses:
                - 201:
                    description: Ajout de tous le solde de `player` à la valeur du bet sur `ia_champion`
                - 404:
                    description: le joueur n'existe pas
                - 500:
                    description: erreur du serveur
        """
        return {"message":f"POST bets/{player}/{ChampionEnum(ia_champion)}/allin"}, 200
