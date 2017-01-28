class Player:

    def __init__(self):
        self.symbol = 'X'
        self.turns = 0

    def print_symbol(self):
        print self.symbol

    def reset_turns(self):
        self.turns = 0

    def increment_turn(self):
        self.turns += 1

    def print_turns(self):
        print self.turns
