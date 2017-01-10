def win(spots):
    if spots[0]==spots[1] and spots[2]==spots[1]:
        return True
    elif spots[3]==spots[4] and spots[5]==spots[4]:
        return True
    elif spots[6]==spots[7] and spots[8]==spots[7]:
        return True
    elif spots[0]==spots[3] and spots[3]==spots[6]:
        return True
    elif spots[7]==spots[4] and spots[4]==spots[1]:
        return True
    elif spots[2]==spots[8] and spots[5]==spots[2]:
        return True
    elif spots[0]==spots[4] and spots[4]==spots[8]:
        return True
    elif spots[2]==spots[4] and spots[4]==spots[6]:
        return True
    return False
