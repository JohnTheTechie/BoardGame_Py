
from Enumerations.Types import MovementStrategyType as MType
from Error import InvalidMovementStrategyError

class MoveCountStrategy:

    strategyType = None

    def __init__(self, type = None):
        if type is None:
            raise InvalidMovementStrategyError
        else:
            self.strategyType = type

class SnakePlayerDestCellRetentionPolicy:
    '''
    defines the logic used for deciding the final move of the player object
    '''

