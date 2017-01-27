class Player:

    total_turns = 0
    total_players = 0

    def __init__(self, symbol):
        self.symbol = symbol
        self.turns = 0
        Player.total_players += 1
        if Player.total_players == 1:
            self.player_turn = True
        elif Player.total_players == 2:
            self.player_turn = False
        else:
            raise Exception("Invalid number of players", Player.total_players)

    def print_symbol(self):
        print self.symbol

    def print_turns(self):
        print self.turns

    def toggle_turns(self):
        self.player_turn = not self.player_turn

    @staticmethod
    def print_total_turns():
        print Player.total_turns
