import random
import os

def initialize_game():
    mat = [[0] * 4 for _ in range(4)]
    add_new_2(mat)
    add_new_2(mat)
    return mat

def add_new_2(mat):
    r, c = random.randint(0, 3), random.randint(0, 3)
    while mat[r][c] != 0:
        r, c = random.randint(0, 3), random.randint(0, 3)
    mat[r][c] = 2

def compress(mat):
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
    return mat

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def move_left(mat):
    mat = compress(mat)
    mat = merge(mat)
    mat = compress(mat)
    return mat

def move_right(mat):
    mat = reverse(mat)
    mat = compress(mat)
    mat = merge(mat)
    mat = compress(mat)
    mat = reverse(mat)
    return mat

def move_up(mat):
    mat = transpose(mat)
    mat = compress(mat)
    mat = merge(mat)
    mat = compress(mat)
    mat = transpose(mat)
    return mat

def move_down(mat):
    mat = transpose(mat)
    mat = reverse(mat)
    mat = compress(mat)
    mat = merge(mat)
    mat = compress(mat)
    mat = reverse(mat)
    mat = transpose(mat)
    return mat

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER'
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'
    return 'LOST'

def print_mat(mat):
    os.system('clear')
    for row in mat:
        print('\t'.join([str(num) if num != 0 else '.' for num in row]))
        print()

def main():
    mat = initialize_game()
    print_mat(mat)
    while True:
        x = input("Press the command (W, A, S, D) for Up, Left, Down, and Right respectively: ")
        if x == 'W' or x == 'w':
            mat = move_up(mat)
        elif x == 'S' or x == 's':
            mat = move_down(mat)
        elif x == 'A' or x == 'a':
            mat = move_left(mat)
        elif x == 'D' or x == 'd':
            mat = move_right(mat)
        else:
            print("Invalid Key Pressed")
            continue
        add_new_2(mat)
        print_mat(mat)
        status = get_current_state(mat)
        if status == 'WON':
            print("You Won!")
            break
        if status == 'LOST':
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
