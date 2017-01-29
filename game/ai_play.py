import random


class AI:

    win_choice = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
    win_occ = {0: 3, 1: 2, 2: 3, 3: 2, 4: 4, 5: 2, 6: 3, 7: 2, 8: 3}

    def __init__(self):
        self.symbol = 'O'

    def ai(self, t):
        return self.check_positions(t)

    def check_positions(self, t):
        temp = 0
        result = -1
        position_options = [0,1,2,3,4,5,6,7]
        for i in AI.win_choice:
            if type(t[i[0]]) != int and type(t[i[1]]) != int and type(t[i[2]]) == int:
                if t[i[0]] == t[i[1]]:
                    if t[i[0]] == self.symbol:
                        return i[2]
                    else:
                        result = i[2]
                else:
                    position_options[temp] = -1
            elif type(t[i[0]]) != int and type(t[i[2]]) != int and type(t[i[1]]) == int:
                if t[i[0]] == t[i[2]]:
                    if t[i[0]] == self.symbol:
                        return i[1]
                    else:
                        result = i[1]
                else:
                    position_options[temp] = -1
            elif type(t[i[1]]) != int and type(t[i[2]]) != int and type(t[i[0]]) == int:
                if t[i[1]] == t[i[2]]:
                    if t[i[1]] == self.symbol:
                        return i[0]
                    else:
                        result = i[0]
                else:
                    position_options[temp] = -1
            temp += 1
        if result < 0:
            result = random.randint(0,8)
            while type(t[result]) != int:
                result = random.randint(0, 8)
        print position_options
        return result