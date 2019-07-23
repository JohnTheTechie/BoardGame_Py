

class Errors(Exception):
    '''
    Base class for all the exceptions used in this project
    '''
    pass

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

class InvalidMovementStrategyError(Errors):
    '''
    raised when creating a strategy object, invalid type is passed

    Attributes:
        type -- the type passed to the object
        message -- explanation
    '''

    def __init__(self, type, message):
        self.type = type
        self.message = message
