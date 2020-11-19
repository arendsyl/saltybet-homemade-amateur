from app import api

from app.resources.shape import DataFrameShape
from app.resources.players.player_rsa import PlayerRSA
from app.resources.players.players_actions import PlayerActions
from app.resources.players.players_info import PlayersInfo
from app.resources.bets.bets_allin import BetsAllIn
from app.resources.bets.bets_actions import BetsAction
from app.resources.bets.bets_info import BetsInfo
from app.resources.bet_multiplier.bet_multiplier import BetMultiplierInfo

# Add every routes of the project
api.add_resource(DataFrameShape, '/api/shape')
api.add_resource(BetMultiplierInfo, '/api/bet_multiplier')
api.add_resource(PlayersInfo, '/api/players')
api.add_resource(PlayerActions, '/api/players/<string:player>')
api.add_resource(PlayerRSA, '/api/players/<string:player>/rsa')
api.add_resource(BetsInfo, '/api/bets')
api.add_resource(BetsAction, '/api/bets/<string:player>/<int:ia_champion>/<float:amount>')
api.add_resource(BetsAllIn, '/api/bets/<string:player>/<int:ia_champion>/allin')