
class BaseCell:

    def __init__(self, next=None, prev=None, listener=None):
        self.next_cell = next
        self.prev_cell = prev
        self.listener = listener
        self.occupant_list = []

    def pushInPlayer(self, player):
        self.occupant_list.append(player)

    def pushOutPlayer(self, player):
        pass

