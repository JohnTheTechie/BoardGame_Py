

class PlayerStatus(enumerate):
    '''
    enumeration of the possible player status
    '''
    PStatus_OUT_OF_BOARD = 1
    PStatus_IDLE = 2
    PStatus_DICE_ROLLING = 3
    PStatus_OPERATION_UNDERWAY = 4
    PStatus_OPERATION_COMPLETED = 5
    PStatus_MOVEMENT_IN_PROGRESS = 6
    PStatus_MOVEMENT_COMPLETED = 7
