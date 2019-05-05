def next_move(posy, posx, dimx, dimy, board):
    if board[posy][posx] == "d":
        move = "CLEAN"
    else:
        d_r, d_c = get_closest_dirt_coords(posy, posx, board)
        move = move_given_coords(posy, posx, d_r, d_c)
    print(move)
    
def get_closest_dirt_coords(posr, posc, board):
    min_dist = None
    d_r = None
    d_c = None
    for i, line in enumerate(board):
        for j, char in enumerate(line):
            if char == "d":
                dist = abs(posr - i) + abs(posc - j)
                if min_dist is None or dist < min_dist:
                    min_dist = dist
                    d_r = i
                    d_c = j
    return d_r, d_c
    
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
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
