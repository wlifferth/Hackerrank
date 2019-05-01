#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    for inv_y, line in enumerate(grid):
        if "p" in line:
            p_r = n - inv_y
            p_c = line.find("p")
        if "m" in line:
            m_r = n - inv_y
            m_c = line.find("m")
    if p_r > m_r:
        for up_move in range(p_r - m_r):
            print("UP")
    elif p_r < m_r:
        for down_move in range(m_r - p_r):
            print("DOWN")
    if p_c > m_c:
        for right_move in range(p_c - m_c):
            print("RIGHT")
    elif p_c < m_c:
        for left_move in range(m_c - p_c):
            print("LEFT")

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
