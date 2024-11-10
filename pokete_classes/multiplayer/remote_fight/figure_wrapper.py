import bs_rpc
from pokete_classes.context import Context
from pokete_classes.fight.fight_decision import FightDecision
from pokete_classes.fight.fightmap.fightmap import FightMap
from pokete_classes.fight.providers import Provider
from pokete_classes.multiplayer.msg import fight


class FigureWrapperProvider(Provider):
    def __init__(self, figure, outgoing: bs_rpc.ResponseWriter):
        self.outgoing = outgoing
        self.figure = figure
        super().__init__(figure.pokes, figure.escapable, figure.xp_multiplier)

    @property
    def caught_pokes(self):
        return self.figure.caught_pokes

    @property
    def map(self):
        return self.figure.map

    def greet(self, fightmap: FightMap):
        return super().greet(fightmap)

    def get_decision(self, ctx: Context, fightmap: FightMap, enem
    ) -> FightDecision:
        result = self.figure.get_decision(ctx, fightmap, enem)
        self.outgoing(fight.FightDecision(result.to_dict()))
        return result

    def handle_defeat(self, ctx: Context, fightmap, winner):
        self.figure.handle_defeat(ctx, fightmap, winner)
