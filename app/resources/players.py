from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

class PlayersInfo(Resource):
    
    def get(self)-> Dict[str, Any]:
        return {"message":"GET players"}, 200


class PlayerActions(Resource):

    def get(self, player: str) -> Dict[str, Any]:
        return {"message":f"GET players/{player}"}, 200

    def post(self, player: str)-> Dict[str, Any]:
        return {"message":f"POST players/{player}"}, 200


class PlayerRSA(Resource):

    def put(self, player: str)-> Dict[str, Any]:
        return {"message":f"PUT players/{player}/rsa"}, 200