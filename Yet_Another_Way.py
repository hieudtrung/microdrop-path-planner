import pygame
import sys
from AStartAlgo import *
import copy
import threading
import time
import pdb
import numpy as np

# Constants
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS, HEIGHT // ROWS

# Colors
YELLOW = (150,150,0)
YELLOW2 = (175, 180, 1)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class drop:
    def __init__(self, from_position, to_position):
        self.from_position = from_position
        self.to_position = to_position

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickable Grid")

# Create a 2D array to store the state of each cell (0: empty, 1: source, 2: destination, 3: path)
#grid_state = [[0 for _ in range(COLS)] for _ in range(ROWS)]
grid_state = np.zeros((ROWS,COLS))
#grid_state = np.arange(100).reshape(10, 10)

for i in range(0,8, 2):
    grid_state[i][4] = 10

THE_GRID = copy.deepcopy(grid_state)
# Variables to store source and destination coordinates
source = None
destination = None


PATH_QUEUE = []
active_paths = []
all_drops = []

def block_kernel(t):
    if(t[0] == 0 and t[1] == 0):
        idx = np.where(grid_state[t[0]:t[0]+2, t[1]: t[1]+2] < 9)
        grid_state[t[0]:t[0]+2, t[1]: t[1]+2][idx] += 1
    elif(t[0] == 0):
        idx = np.where(grid_state[t[0]:t[0]+2, t[1]-1: t[1]+2] < 9)
        grid_state[t[0]:t[0]+2, t[1]-1: t[1]+2][idx] += 1
        
    elif(t[1] == 0):
        idx = np.where(grid_state[t[0]-1:t[0]+2, t[1]: t[1]+2] < 9)
        grid_state[t[0]-1:t[0]+2, t[1]: t[1]+2][idx] += 1
    else:
        idx = np.where(grid_state[t[0]-1:t[0]+2, t[1]-1: t[1]+2] < 9)
        grid_state[t[0]-1:t[0]+2, t[1]-1: t[1]+2][idx] += 1




def un_block_kernel(t):
    if(t[0] == 0 and t[1] == 0):
        idx = np.where(grid_state[t[0]:t[0]+2, t[1]: t[1]+2] < 9)
        grid_state[t[0]:t[0]+2, t[1]: t[1]+2][idx] -= 1
        
    elif(t[0] == 0):
        idx = np.where(grid_state[t[0]:t[0]+2, t[1]-1: t[1]+2] < 9)
        grid_state[t[0]:t[0]+2, t[1]-1: t[1]+2][idx] -= 1
    elif(t[1] == 0):
        idx = np.where(grid_state[t[0]-1:t[0]+2, t[1]: t[1]+2] < 9)
        grid_state[t[0]-1:t[0]+2, t[1]: t[1]+2][idx] -= 1
    else:
        idx = np.where(grid_state[t[0]-1:t[0]+2, t[1]-1: t[1]+2] < 9)
        grid_state[t[0]-1:t[0]+2, t[1]-1: t[1]+2][idx] -= 1
    
    
def my_function():
    prev = None
    while 1:
        if len(all_drops):
            for i, j in enumerate(all_drops):
                #print(">>", j.from_position, j.to_position)
                
                if(j.from_position != j.to_position):
                    un_block_kernel(j.from_position)
                    this_path = astar(j.from_position, j.to_position, grid_state)
                    if this_path:
                        #print(this_path)
                        
                        j.from_position = this_path[1]
                               
                        grid_state[this_path[0][0]][this_path[0][1]] = 0
                        grid_state[this_path[1][0]][this_path[1][1]] = 9

                        #block_kernel(j.from_position)
                        #pdb.set_trace()
                        
                    else:
                        print("Path Not Found", j.from_position, j.to_position)
                        
                        #grid_state[j.from_position[0]][j.from_position[1]] = 9
                        pass

                        #block_kernel(j.from_position)
                    block_kernel(j.from_position)
                        
                
            time.sleep(0.1)

my_thread = threading.Thread(target=my_function)
my_thread.start()


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // CELL_SIZE[0]
            row = y // CELL_SIZE[1]

            # Left click: Select source
            if event.button == 1:
                #grid_state = copy.deepcopy(THE_GRID)  # Reset grid state
                source = (row, col)
                print(source)
                grid_state[row][col] = 9
                #block_kernel(source)

            # Right click: Select destination and highlight path
            elif event.button == 3 and source:
                destination = (row, col)
                
                if(source != None):
                    found = 0
                    for i in all_drops:
                        if(i.from_position == source):
                            i.to_position = destination
                            found = 1
                            break
                        
                    if(found == 0):
                        print("Drop Created")
                        block_kernel(source)
                        all_drops.append(drop(source, destination))
                        source = None


                    
    # Draw the grid
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if grid_state[row][col] == 0:
                color = WHITE
            elif grid_state[row][col] == 1:
                color = YELLOW
            elif grid_state[row][col] == 2:
                color = YELLOW2
            elif grid_state[row][col] == 9:
                color = BLUE
            elif grid_state[row][col] == 10:
                color = BLACK
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE[0], row * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))

    # Draw grid lines
    for i in range(1, ROWS):
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE[1]), (WIDTH, i * CELL_SIZE[1]))
    for j in range(1, COLS):
        pygame.draw.line(screen, BLACK, (j * CELL_SIZE[0], 0), (j * CELL_SIZE[0], HEIGHT))

    pygame.display.flip()
    #pdb.set_trace()
my_thread.join()
# Quit Pygame
pygame.quit()
sys.exit()
