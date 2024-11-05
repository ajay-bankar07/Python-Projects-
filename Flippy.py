import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flippy')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game settings
FPS = 30
GRID_SIZE = 4  # 4x4 grid
TILE_SIZE = 80
GAP_SIZE = 10

# Calculate margin for centering the grid
MARGIN_X = (WINDOW_WIDTH - (TILE_SIZE + GAP_SIZE) * GRID_SIZE + GAP_SIZE) // 2
MARGIN_Y = (WINDOW_HEIGHT - (TILE_SIZE + GAP_SIZE) * GRID_SIZE + GAP_SIZE) // 2

# Define possible shapes
POSSIBLE_SHAPES = ['circle', 'square', 'diamond', 'oval', 'star', 'triangle', 'heart', 'hexagon']

# Calculate number of shapes needed
NUM_PAIRS = (GRID_SIZE ** 2) // 2
ALL_SHAPES = random.sample(POSSIBLE_SHAPES, NUM_PAIRS)

# Store board state
main_board = []

# Initialize game state
def initialize_board():
    # Create pairs of shapes
    icons = ALL_SHAPES * 2
    random.shuffle(icons)
    
    # Populate the main board with pairs
    for x in range(GRID_SIZE):
        column = []
        for y in range(GRID_SIZE):
            column.append({'shape': icons.pop(), 'revealed': False})
        main_board.append(column)

def draw_tile(x, y, shape, revealed):
    # Calculate position
    left = MARGIN_X + x * (TILE_SIZE + GAP_SIZE)
    top = MARGIN_Y + y * (TILE_SIZE + GAP_SIZE)

    # Draw the tile
    if revealed:
        if shape == 'circle':
            pygame.draw.circle(window, GREEN, (left + TILE_SIZE//2, top + TILE_SIZE//2), TILE_SIZE//2 - 5)
        elif shape == 'square':
            pygame.draw.rect(window, GREEN, (left, top, TILE_SIZE, TILE_SIZE))
        elif shape == 'diamond':
            pygame.draw.polygon(window, GREEN, [(left + TILE_SIZE//2, top), (left + TILE_SIZE, top + TILE_SIZE//2),
                                                (left + TILE_SIZE//2, top + TILE_SIZE), (left, top + TILE_SIZE//2)])
        elif shape == 'oval':
            pygame.draw.ellipse(window, GREEN, (left + 10, top + 20, TILE_SIZE - 20, TILE_SIZE - 40))
    else:
        pygame.draw.rect(window, BLACK, (left, top, TILE_SIZE, TILE_SIZE))

def draw_board():
    window.fill(WHITE)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            tile = main_board[x][y]
            draw_tile(x, y, tile['shape'], tile['revealed'])

def get_tile_at_pixel(x, y):
    for grid_x in range(GRID_SIZE):
        for grid_y in range(GRID_SIZE):
            left = MARGIN_X + grid_x * (TILE_SIZE + GAP_SIZE)
            top = MARGIN_Y + grid_y * (TILE_SIZE + GAP_SIZE)
            tile_rect = pygame.Rect(left, top, TILE_SIZE, TILE_SIZE)
            if tile_rect.collidepoint(x, y):
                return (grid_x, grid_y)
    return None

def main():
    clock = pygame.time.Clock()
    initialize_board()
    
    first_tile = None
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                clicked_tile = get_tile_at_pixel(mouse_x, mouse_y)
                if clicked_tile:
                    x, y = clicked_tile
                    if not main_board[x][y]['revealed']:
                        main_board[x][y]['revealed'] = True
                        if first_tile is None:
                            first_tile = (x, y)
                        else:
                            second_tile = (x, y)
                            if main_board[first_tile[0]][first_tile[1]]['shape'] == main_board[second_tile[0]][second_tile[1]]['shape']:
                                first_tile = None
                            else:
                                pygame.time.wait(1000)
                                main_board[first_tile[0]][first_tile[1]]['revealed'] = False
                                main_board[second_tile[0]][second_tile[1]]['revealed'] = False
                                first_tile = None

        draw_board()
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
