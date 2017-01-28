import random


class AI:

    win_choice = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

    def __init__(self):
        self.symbol = 'O'

    def ai(self, t):
        return self.check_positions(t)

    def check_positions(self, t):
        result = 4
        for i in AI.win_choice:
            if t[i[0]] == t[i[1]] and type(t[i[2]]) == int:
                if t[i[0]] == self.symbol:
                    return i[2]
                else:
                    result = i[2]
            elif t[i[0]] == t[i[2]] and type(t[i[1]]) == int:
                if t[i[0]] == self.symbol:
                    return i[1]
                else:
                    result = i[1]
            elif t[i[1]] == t[i[2]] and type(t[i[0]]) == int:
                if t[i[1]] == self.symbol:
                    return i[0]
                else:
                    result = i[0]
        while type(t[result]) != int:
            result = random.randint(0, 8)
        return result