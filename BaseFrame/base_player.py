from Enumerations.States import PlayerStatus

class BasePlayer:

    def __init__(self, occupying_cell = None, current_status=PlayerStatus.PStatus_OUT_OF_BOARD):
        self.occupying_cell = occupying_cell
        self.status = current_status
