from Enumerations.States import PlayerStatus
from Error import InvalidMoveCountUpdateError

class BasePlayer:

    def __init__(self, occupying_cell = None, current_status=PlayerStatus.PStatus_OUT_OF_BOARD):
        self.occupying_cell = occupying_cell
        self.status = current_status
        self.remaining_moves = 0

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status  =status

    def setRemainingMoves(self, move_count = None):
        if move_count is None:
            raise InvalidMoveCountUpdateError(move_count, "None is not a valid move count")
        elif move_count < 0:
            raise InvalidMoveCountUpdateError(move_count, "count cannot be negative")
        #TODO: add movecount strategy clause
