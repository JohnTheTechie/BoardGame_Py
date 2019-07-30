

class Errors(Exception):
    '''
    Base class for all the exceptions used in this project
    '''
    pass

class CellErrors(Errors):
    '''
    Base class for errors raised by cells.
    extends Errors
    Attributes:
        cell - Index of the raising cell in integer value
        Message - explanation for the issue
    '''

    def __init__(self, cell, message):
        self.cell = cell
        self.message = message
        print(f"{cell} : {message}")

class InvalidMovementStrategyError(CellErrors):
    '''
    raised when creating a strategy object, invalid type is passed

    Attributes:
        cell - Index of the raising cell in integer value
        type -- the type passed to the object
        message -- explanation
    '''

    def __init__(self,cell, type, message):
        super().__init__(cell, message)
        self.type = type


class NonExistentOccupant(CellErrors):
    '''
    raised when a nonoccupant is tried to be accessed from the cell
    Attributes:
        cell - Index of the raising cell in integer value
        Player - Index of the player accessed
        Message - explanation for the issue

    '''

    def __init__(self, cell, player, message):
        super().__init__(cell, message)
        self.player = player


########################################################################

class InvalidMoveCountUpdateError(Errors):
    '''
    raised when an invalid move count is passed to the player object

    attributes:
        count - move count passed to the object
        message - explanation of the issue
    '''

    def __init__(self, count, message):
        self.count = count
        self.message = message


