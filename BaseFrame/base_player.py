from Enumerations.States import PlayerStatus
from Error import InvalidMoveCountUpdateError
import logging

class BasePlayer:
    """
    defines the base class for the player object
    """

    counter = 0

    def __init__(self, occupying_cell = None, current_status=PlayerStatus.PStatus_OUT_OF_BOARD):
        self.occupying_cell = occupying_cell
        self.status = current_status
        self.remaining_moves = 0
        self.index, self.counter = self.counter+1, self.counter+1
        logging.info(f"{__name__} | index = {self.index} | player object created")

    def __str__(self):
        return BasePlayer.__name__+" | index = " + str(self.index) + " | "

    def setOccupyingCell(self, cell):
        """
        store the reference to the cell currently occupied by the player
        :param cell: currently occupied cell
        :return: None
        """
        self.occupying_cell = cell
        logging.info(f"{__name__} | index = {self.index} | occupying cell updated to cell-{self.occupying_cell.index}")

    def getStatus(self):
        """
        returns the status of the player
        :return: status
        """
        logging.info(f"{__name__} | index = {self.index} | status of the player read as {self.status}")
        return self.status

    def setStatus(self, status):
        """
        update the status of the player
        :param status: current status
        :return: None
        """
        self.status = status
        logging.info(f"{__name__} | index = {self.index} | status of the player changed to {self.status}")

    def setRemainingMoves(self, move_count=None):
        """
        called by the dice to set the moves entitles to the player
        cell count could be a list of move counts or a single integer number
        :param move_count: dice output
        :return: None
        """
        if move_count is None:
            logging.error(f"{__name__} | index = {self.index} | move count invalid - set to None")
            raise InvalidMoveCountUpdateError(move_count, "None is not a valid move count")
        elif move_count < 0:
            logging.error(f"{__name__} | index = {self.index} | invalid move count passed - negative moves")
            raise InvalidMoveCountUpdateError(move_count, "count cannot be negative")
        else:
            self.remaining_moves = move_count
            logging.error(f"{__name__} | index = {self.index} | move count set to {self.remaining_moves}")


