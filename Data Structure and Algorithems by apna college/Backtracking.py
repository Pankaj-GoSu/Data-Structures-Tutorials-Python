#======== Backtracking ============

'''
Backtracking is an algorithmic technique for solving recursive problems by trying to build 
every possible solution incremently and removing those solutions that fails to satisfy the 
constraints of the problem at any point of time.

'''

# Problem

'''
Rat in a maze
'''
sol = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def issafe(maze,x,y):

    if x >= 0 and x < len(maze) and y>=0 and y < len(maze[0]) and maze[x][y] ==1:
        return True
    return False

def maze_sol(maze,x,y):

    if x == len(maze) and y == len(maze[0]):
        sol[x][y] = 1

    if issafe(maze,x,y) == True:
        sol[x][y] = 1
        maze_sol(maze,x+1,y)
        
        maze_sol(maze,x,y+1)

# maze = [ [1, 0, 0, 0],
#              [1, 1, 0, 1],
#              [0, 1, 0, 0],
#              [1, 1, 1, 1] ]

maze = [[1,0,1,0,1],[1,1,1,1,1],[0,1,0,1,0],[1,0,0,1,1],[1,1,1,0,1]]
maze_sol(maze,0,0)
print(sol)