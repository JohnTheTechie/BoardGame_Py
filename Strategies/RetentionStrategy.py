

import logging

class FinalCellPlayerRetentionPolicy:
    """
    Base class to define the interface for the retention policy classes
    Should be extended first before usage
    """
    __StrategyObject = None

    def is_player_retainable_in_the_cell(self, cell, player):
        pass

class SnakePlayerRetention(FinalCellPlayerRetentionPolicy):
    """
    Retention policy for the Snakes and Ladders games
    Decides if the cell should retain the player
    If the cell has no banching option, player shall be pushed into the cell
    If defined, the player will be moved to the
    """

    def __new__(cls, *args, **kwargs):
        """
        defines singleton for policy
        :param args:
        :param kwargs:
        :return:
        """
        if cls.__StrategyObject is None:
            cls.__StrategyObject = object.__new__(cls)
        return cls.__StrategyObject

    def is_player_retainable_in_the_cell(self, cell, player):
        """
        checks whether the player could be retained or further moved.
        if retainable return (True, None)
        else return (False, next cell to move the player)
        :param cell: calling cell
        :param player:
        :return:
        """
        super().is_player_retainable_in_the_cell(cell, player)
        if player.remaining_moves == 0:
            if cell.branching is None:
                logging.info(f"{__name__} | cell index = {cell.index} | player-{player.index} can be retained")
                return True, None
            else:
                logging.info(f"{__name__} | cell index = {cell.index} | player-{player.index} can not be retained | move to {cell.branching}")
                return False, cell.branching
        else:
            logging.info(f"{__name__} | cell index = {cell.index} | player-{player.index} can not be retained | move to {cell.next_cell} ")
            return False, cell.next_cell
