from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

class PlayerActions(Resource):

    def get(self, player: str) -> Dict[str, Any]:
        return {"message":f"GET players/{player}"}, 200

    def post(self, player: str) -> Dict[str, Any]:
        return {"message":f"POST players/{player}"}, 200

    def delete(self, player) -> Dict[str, Any]:
        return {"message": f"DELETE players/{player}"}, 200
