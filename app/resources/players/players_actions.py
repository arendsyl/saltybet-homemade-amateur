from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

class PlayerActions(Resource):

    def get(self, player: str) -> Dict[str, Any]:
        """
        Retourne un dictionnaire avec en clé le nom du joueur, en valeur son solde.
        Erreur 404 si le joueur n'existe pas.
        200 si OK, 500 si erreur.
        ---
            tags:
                - Route pour les joueurs
            responses:
                - 200:
                    description: Le joueur est bien renvoyé
                - 404:
                    description: Le joueur n'existe pas
                - 500:
                    description: Erreur du serveur
        """
        return {"message":f"GET players/{player}"}, 200

    def post(self, player: str) -> Dict[str, Any]:
        """
        Crée le joueur en base, avec un solde de 1000.
        201 si OK, 200 si le joueur existe déjà, 500 si erreur.
        ---
            tags:
                - Route pour les joueurs
            responses:
                - 201:
                    description: Le joueur a bien été créé avec un solde de 1000
                - 200:
                    description: Le joueur existe déjà
                - 500:
                    description: Erreur du serveur
        """
        return {"message":f"POST players/{player}"}, 200

    def delete(self, player) -> Dict[str, Any]:
        """
        Supprime le joueur de la base, ses bets actifs et son solde.
        200 si OK, 404 si le joueur n'existe pas, 500 si erreur.
        ---
            tags:
                - Route du MJ
            parameters:
                - in: body
                    name: auth_token
                    description: Token d'authentification du MJ
                    required: true
                    type: string
            responses:
                - 200:
                    description: Le joueur a bien été supprimé
                - 404:
                    description: Le joueur n'existe pas
                - 500:
                    description: Erreur du serveur
        """
        return {"message": f"DELETE players/{player}"}, 200
