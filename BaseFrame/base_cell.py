
import logging
import Error


class BaseCell:
    '''
    Baseclass for the cell object is defined here
    Bse classs will support to store next and previous cells, branching cell if needed.
    It will maintain a list of players occupying the cell
    '''
    movementStrategy = None
    counter = 0

    def __init__(self, next=None, prev=None):
        self.index, self.counter = self.counter+1, self.counter+1
        self.next_cell = next
        self.prev_cell = prev
        self.occupant_list = []
        self.branching = None
        logging.info(f"Base cell object created | index={self.index}")

    def setBranchingInfo(self, branchingCell):
        """
        set branching cell if needed.
        If the branching parameter is set to none, the cell will be assumed as a normal cell
        :param branchingCell: destination cell to which the player might be moved
        :return: None
        """
        self.branching = branchingCell
        logging.info(f"{__name__} | index = {self.index} | branching set to cell {self.branching.index}")

    def setMovementStraegy(self, strategy):
        """
        set movement strategy object.
        That object will be used to decide if the player
        reaching the cell should be retained or moved to the branching cell
        :param strategy: strategy object
        :return: None
        """
        self.movementStrategy = strategy
        logging.info(f"{__name__} | index = {self.index} | strategy set")

    def pushInPlayer(self, player):
        """
        called by the board to push-in a player object to the occupant list
        :param player: player to be pushed in
        :return: None if retained, cell reference if movement needed
        """
        retainability, next_stop = self.movementStrategy.is_player_retainable_in_the_cell(self, player)
        if retainability:
            self.occupant_list.append(player)
            player.occupant_cell.pushOutPlayer(player)
            player.occupant_cell = self
            logging.info(f"{__name__} | index = {self.index} | player {player.index} pushed in")
            return None
        else:
            return next_stop


    def pushOutPlayer(self, player):
        """
        called by the board to remove a player from the occupant list.
        If the player is not an occupant Exception shall be raised
        :param player: Player to be checked
        :return: None
        """
        if player in self.occupant_list:
            self.occupant_list.remove(player)
            logging.info(f"{__name__} | index = {self.index} | player {player.index} pushed out")
        else:
            logging.warning(f"{__name__} | index = {self.index} | player {player.index} tried to be pushed out, player not an occupant")
            raise Error.NonExistentOccupant


