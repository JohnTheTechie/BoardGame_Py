
from Strategies.PlayerMoveCountStrategy import MoveCountStrategy
import Error


class BaseCell(MoveCountStrategy):
    '''

    '''
    MovementStrategy = None

    def __init__(self, next=None, prev=None, listener=None):
        self.next_cell = next
        self.prev_cell = prev
        self.listener = listener
        self.occupant_list = []
        self.branching = None

    def setBranchingInfo(self, branchingCell):
        self.branching = branchingCell

    def setMovementStraegy(self, strategy):
        self.MovementStrategy = strategy

    def pushInPlayer(self, player):
        self.occupant_list.append(player)

    def pushOutPlayer(self, player):
        if player in self.occupant_list:
            self.occupant_list.remove(player)
        else:
            raise Error.NonExistentOccupant


