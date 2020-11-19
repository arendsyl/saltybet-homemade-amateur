from flask import request
from flask_restful import Resource, reqparse

import typing
from typing import Dict, Any

class BetMultiplierInfo(Resource):

    def get(self):
        return {"message": "GET bet_multiplier"}, 200