from app import api

from app.resources.shape import DataFrameShape
from app.resources.init import Init
from app.resources.bets.bets_open import BetsOpen
from app.resources.bets.bets_close import BetsClose
from app.resources.bets.bets_resolve import BetsResolve
from app.resources.bet_multiplier.bet_multiplier_change import (
    BetMultiplierChange
)

# Add every routes of the project
# TODO : supprimer la route shape, dès qu'on aura plus
# besoin d'un modèle 
api.add_resource(DataFrameShape, '/api/shape')
api.add_resource(Init, '/init')
api.add_resource(BetsOpen, '/open_bets')
api.add_resource(BetsClose, '/bets/close')
api.add_resource(BetsResolve, '/bets/resolve/<int:champion>')
api.add_resource(BetMultiplierChange, '/bet_multiplier/<float:facteur>')
