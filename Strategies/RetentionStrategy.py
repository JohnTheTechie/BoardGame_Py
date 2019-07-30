
class FinaCellPlayerRetentionPolicy:

    def is_player_retainable_in_the_cell(self, cell, player):
        pass

class SnakePlayerRetention(FinaCellPlayerRetentionPolicy):

    def is_player_retainable_in_the_cell(self, cell, player):
        super().is_player_retainable_in_the_cell(cell, player)
        if cell.branching is None:
            cell.occupant_list.append(player)
        else:
            self.cell.branching.pushInPlayer(player)
        player.occupant_cell.pushOutPlayer(player)
        player.occupant_cell = cell