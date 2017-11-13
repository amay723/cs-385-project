import sys


def main():

    grid = [[" " for x in range(3)] for y in range(3)]

    while( True ):
        Xturn = input("X move: ")

        x = int(Xturn[0])
        y = int(Xturn[-1])

        if( grid[x][y] is not "O" and grid[x][y] is not "X" ):
            grid[x][y] = "X"
        else:
            print("Move error")

        for i in range(0,3):
            for j in range(0,3):
                print(grid[i][j], end=' ')
            print()

        Yturn = input("Y move: ")

        x = int(Yturn[0])
        y = int(Yturn[-1])

        if( grid[x][y] is not "O" and grid[x][y] is not "X" ):
            grid[x][y] = "Y"
        else:
            print("Move error")

        for i in range(0,3):
            for j in range(0,3):
                print(grid[i][j], end=' ')
            print()







main()