from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

from app.features.ia_champion import ChampionEnum

class BetsAction(Resource): 

    def post(self, player: str, ia_champion: int, amount: float)-> Dict[str, Any]:
        """
        Le joueur `player` (str) place un `bet` (float) sur le `ia_champion` (int mais valeurs uniquement possibles : 1 ou 2).
        201 si OK (ajout à la valeur du bet déjà existant si un bet a déjà été placé).
        402 si le bet est plus gros que le solde du joueur.
        404 si le joueur n'existe pas.
        500 si erreur.
        ---
            tags: 
                - Route pour les joueurs
            responses:
                - 201:
                    description: Ajout de `amount` à la valeur du bet sur `ia_champion` par `player`
                - 402:
                    description: `amout` est plus gros que le solde de `player`
                - 404:
                    description: le joueur n'existe pas
                - 500:
                    description: erreur du serveur
        """
        # TODO : index overflow/underflow on ChampionEnum
        return {"message":f"POST bets/{player}/{ChampionEnum(ia_champion)}/{amount}"}, 200
