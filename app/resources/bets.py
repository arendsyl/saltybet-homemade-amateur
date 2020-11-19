from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

from app.features.ia_champion import ChampionEnum

class BetsInfo(Resource):

    def get(self):
        return {"message": "GET bets"}, 200

class BetsAction(Resource): 

    def post(self, player: str, ia_champion: int, amount: float):
        # TODO : index overflow/underflow on ChampionEnum
        return {"message":f"POST bets/{player}/{ChampionEnum(ia_champion)}/{amount}"}, 200

class BetsAllIn(Resource):
    def post(self, player: str, ia_champion: int):
        return {"message":f"POST bets/{player}/{ChampionEnum(ia_champion)}/allin"}