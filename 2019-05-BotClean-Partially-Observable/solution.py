#!/usr/bin/python3

def next_move(bot_r, bot_c, board):
    if board[bot_r][bot_c] == "d":
        print("CLEAN")
        return
    next_r, next_c = get_next_coords(bot_r, bot_c)
    print(move_given_coords(bot_r, bot_c, next_r, next_c))
    return

def get_next_coords(bot_r, bot_c):
    # On even rows
    if bot_r % 2 == 0:
        if bot_c < 4:
            return (bot_r, bot_c + 1)
        else:
            return (bot_r + 1, bot_c)
    # On odd rows
    if bot_r % 2 == 1:
        if bot_c > 0:
            return (bot_r, bot_c - 1)
        else:
            return (bot_r + 1, bot_c)

def move_given_coords(b_r, b_c, d_r, d_c):
    if b_r > d_r:
        return "UP"
    elif b_r < d_r:
        return "DOWN"
    elif b_c > d_c:
        return "LEFT"
    elif b_c < d_c:
        return "RIGHT"
    else:
        return None

def abs(x):
    if x < 0:
        return -x
    else:
        return x

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
