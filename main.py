import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Load and scale the icon image for the main menu
menu_icon_image = pygame.image.load('Assets/ship_horizontal.png')
icon_size = (150, 150)  # Adjust the size as desired
menu_icon_image = pygame.transform.scale(menu_icon_image, icon_size)

# Set the window icon (small icon in title bar)
icon_image = pygame.image.load('Assets/ship_horizontal.png')
pygame.display.set_icon(icon_image)

# CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
GRID_SIZE = 10
MARGIN = 50
SPACING_BETWEEN_GRIDS = 50

# Calculate CELL_SIZE to fit both grids within the screen width
CELL_SIZE = (SCREEN_WIDTH - 2 * MARGIN - SPACING_BETWEEN_GRIDS) // (2 * GRID_SIZE)

# Recalculate GRID_WIDTH and positions
GRID_WIDTH = GRID_SIZE * CELL_SIZE
player_grid_x = MARGIN
player_grid_y = MARGIN + 50  # Slight adjustment to accommodate the title
ai_grid_x = player_grid_x + GRID_WIDTH + SPACING_BETWEEN_GRIDS
ai_grid_y = MARGIN + 50

# Colors
WHITE = (255, 255, 255)    # Background overlay color
BLACK = (0, 0, 0)          # Grid lines
BLUE = (30, 144, 255)      # Ships (Dodger Blue)
GRAY = (169, 169, 169)     # Miss (Dark Gray)
RED = (220, 20, 60)        # Hit (Crimson)

# Ship sizes
SHIP_SIZES = [5, 4, 3, 3, 2]

# AI targeting state
ai_targets = []

# Screen setup
pygame.display.set_caption("Battleship")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load background image
background_image = pygame.image.load('Assets/background.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define fonts globally
FONT_SMALL = pygame.font.SysFont('Arial', 24)
FONT_LARGE = pygame.font.SysFont('Arial', 60)

# Ship class
class Ship:
    def __init__(self, size):
        self.size = size
        self.coordinates = []
        self.orientation = None
        self.hits = 0
        
    def is_sunk(self):
        return self.hits == self.size
        
    def hit(self):
        self.hits += 1

# Main Menu function
def main_menu():
    menu_running = True

    # Fonts
    title_font = pygame.font.SysFont('Arial', 60)
    button_font = pygame.font.SysFont('Arial', 40)

    # Define button rectangles
    button_width = 200
    button_height = 50
    normal_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, 200, button_width, button_height)
    hard_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, 300, button_width, button_height)
    quit_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, 400, button_width, button_height)

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if buttons are clicked
                if normal_button.collidepoint(mouse_x, mouse_y):
                    return 'normal'
                elif hard_button.collidepoint(mouse_x, mouse_y):
                    return 'hard'
                elif quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        # Draw the menu
        # Replace filling the screen with blitting the background image
        # screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        # Draw title
        title_text = title_font.render('Battleship', True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title_text, title_rect)

        # Draw buttons
        pygame.draw.rect(screen, BLUE, normal_button)
        pygame.draw.rect(screen, BLUE, hard_button)
        pygame.draw.rect(screen, BLUE, quit_button)

        # Draw button text
        normal_text = button_font.render('Normal Mode', True, WHITE)
        normal_text_rect = normal_text.get_rect(center=normal_button.center)
        screen.blit(normal_text, normal_text_rect)

        hard_text = button_font.render('Hard Mode', True, WHITE)
        hard_text_rect = hard_text.get_rect(center=hard_button.center)
        screen.blit(hard_text, hard_text_rect)

        quit_text = button_font.render('Quit', True, WHITE)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_text_rect)

        # Update the display
        pygame.display.flip()

# Game Over Screen function
def game_over_screen(winner):
    over_running = True

    # Fonts
    over_font = pygame.font.SysFont('Arial', 60)
    button_font = pygame.font.SysFont('Arial', 40)

    # Define buttons
    button_width = 200
    button_height = 50
    restart_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, 300, button_width, button_height)
    quit_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, 400, button_width, button_height)

    if winner == 'player':
        over_text = over_font.render('You Win!', True, WHITE)
    else:
        over_text = over_font.render('Game Over', True, WHITE)
    over_rect = over_text.get_rect(center=(SCREEN_WIDTH // 2, 150))

    while over_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over_running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_x, mouse_y):
                    return True  # Player wants to play again
                elif quit_button.collidepoint(mouse_x, mouse_y):
                    over_running = False
                    pygame.quit()
                    sys.exit()

        # Draw the game over screen
        # Replace filling the screen with blitting the background image
        # screen.fill(BLACK)
        screen.blit(background_image, (0, 0))

        # Draw the winner message
        screen.blit(over_text, over_rect)

        # Draw buttons
        pygame.draw.rect(screen, BLUE, restart_button)
        pygame.draw.rect(screen, BLUE, quit_button)

        # Draw button text
        restart_text = button_font.render('Play Again', True, WHITE)
        restart_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_rect)

        quit_text = button_font.render('Quit', True, WHITE)
        quit_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_rect)

        # Update the display
        pygame.display.flip()

# Function to draw ships
def draw_ships(ships, x_start, y_start, cell_size):
    for ship in ships:
        for (row, col) in ship.coordinates:
            rect = pygame.Rect(
                x_start + col * cell_size + 1,
                y_start + row * cell_size + 1,
                cell_size - 2,
                cell_size - 2
            )
            pygame.draw.rect(screen, BLUE, rect)

# Function to draw the grid
def draw_grid(x_start, y_start, grid_size, cell_size):
    # Draw horizontal lines
    for row in range(grid_size + 1):
        pygame.draw.line(screen, BLACK, 
                         (x_start, y_start + row * cell_size),
                         (x_start + grid_size * cell_size, y_start + row * cell_size), 2)  # Thickness of 2
    # Draw vertical lines
    for col in range(grid_size + 1):
        pygame.draw.line(screen, BLACK,
                         (x_start + col * cell_size, y_start),
                         (x_start + col * cell_size, y_start + grid_size * cell_size), 2)  # Thickness of 2

# Function to draw hits and misses
def draw_hits_and_misses(board, x_start, y_start, cell_size):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'H':
                rect = pygame.Rect(
                    x_start + col * cell_size + 1,
                    y_start + row * cell_size + 1,
                    cell_size - 2,
                    cell_size - 2
                )
                pygame.draw.rect(screen, RED, rect)
            elif board[row][col] == 'M':
                rect = pygame.Rect(
                    x_start + col * cell_size + 1,
                    y_start + row * cell_size + 1,
                    cell_size - 2,
                    cell_size - 2,
                )
                pygame.draw.rect(screen, GRAY, rect)

# Function to get adjacent cells
def get_adjacent_cells(row, col, board):
    adjacent = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            if board[r][c] in [' ', 'S']:
                adjacent.append((r, c))
    return adjacent

# Function to place ships randomly
def place_ships_randomly(grid, ships):
    for size in SHIP_SIZES:
        ship_placed = False
        while not ship_placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, GRID_SIZE - 1)
                col = random.randint(0, GRID_SIZE - size)
            else:
                row = random.randint(0, GRID_SIZE - size)
                col = random.randint(0, GRID_SIZE - 1)

            # Assume the ship fits until proven otherwise
            ship_fits = True
            ship_coordinates = []
            for i in range(size):
                if orientation == 'horizontal':
                    if grid[row][col + i] != ' ':
                        ship_fits = False
                        break
                    ship_coordinates.append((row, col + i))
                else:
                    if grid[row + i][col] != ' ':
                        ship_fits = False
                        break
                    ship_coordinates.append((row + i, col))
            if ship_fits:
                # Place the ship
                for coordinates in ship_coordinates:
                    r, c = coordinates
                    grid[r][c] = 'S'
                ship = Ship(size)
                ship.orientation = orientation
                ship.coordinates = ship_coordinates
                ships.append(ship)
                ship_placed = True
                
#Function to place ships manually
def place_ships_manually(board, ships):
    placing_ships = True
    ship_index = 0
    orientation = 'horizontal'  # Default orientation
    status_message = ""

    while placing_ships:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Rotate the ship
                    orientation = 'vertical' if orientation == 'horizontal' else 'horizontal'
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Now check if click is within the player's grid
                if (player_grid_x <= mouse_x < player_grid_x + GRID_WIDTH and
                    player_grid_y <= mouse_y < player_grid_y + GRID_WIDTH):
                    col = int((mouse_x - player_grid_x) // CELL_SIZE)
                    row = int((mouse_y - player_grid_y) // CELL_SIZE)

                    # Attempt to place the ship
                    ship_size = SHIP_SIZES[ship_index]
                    if is_valid_placement(board, row, col, ship_size, orientation):
                        # Place the ship
                        new_ship = Ship(ship_size)
                        new_ship.orientation = orientation
                        for i in range(ship_size):
                            r = row + i if orientation == 'vertical' else row
                            c = col if orientation == 'vertical' else col + i
                            board[r][c] = 'S'
                            new_ship.coordinates.append((r, c))
                        ships.append(new_ship)
                        ship_index += 1
                        if ship_index == len(SHIP_SIZES):
                            placing_ships = False  # All ships placed
                        else:
                            status_message = "Ship placed successfully"
                    else:
                        status_message = "Invalid placement. Try again."

        # Drawing code for ship placement
        # Replace filling the screen with blitting the background image
        screen.blit(background_image, (0, 0))

        # Create a semi-transparent overlay for the grid
        grid_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay_color = (255, 255, 255, 180)  # Adjust the alpha value as needed
        grid_overlay.fill(overlay_color)
        screen.blit(grid_overlay, (0, 0))

        # Draw the player's grid
        draw_grid(player_grid_x, player_grid_y, GRID_SIZE, CELL_SIZE)
        draw_ships(ships, player_grid_x, player_grid_y, CELL_SIZE)

        if ship_index < len(SHIP_SIZES):
            # Draw the ship preview
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (player_grid_x <= mouse_x < player_grid_x + GRID_WIDTH and
                player_grid_y <= mouse_y < player_grid_y + GRID_WIDTH):
                col = int((mouse_x - player_grid_x) // CELL_SIZE)
                row = int((mouse_y - player_grid_y) // CELL_SIZE)
                ship_size = SHIP_SIZES[ship_index]
                draw_ship_preview(screen, row, col, ship_size, orientation, player_grid_x, player_grid_y)

            # Instructions
            font = pygame.font.SysFont('Arial', 24)
            instructions = font.render(
                f'Place your ships. Press R to rotate. Placing ship of size {SHIP_SIZES[ship_index]}',
                True,
                BLACK
            )
            screen.blit(instructions, (50, 20))

        # Render the status message
        status_text = font.render(status_message, True, BLACK)
        status_rect = status_text.get_rect(
            midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10))  # Adjust positioning as needed
        screen.blit(status_text, status_rect)

        # Update the display
        pygame.display.flip()

#Function to check if the ship can be placed
def is_valid_placement(board, row, col, size, orientation):
    for i in range(size):
        r = row + i if orientation == 'vertical' else row
        c = col if orientation == 'vertical' else col + i
        if r >= GRID_SIZE or c >= GRID_SIZE:
            return False
        if board[r][c] == 'S':
            return False
    return True

#Function to draw ship preview
def draw_ship_preview(screen, row, col, size, orientation, grid_x, grid_y):
    for i in range(size):
        r = row + i if orientation == 'vertical' else row
        c = col if orientation == 'vertical' else col + i
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            x = grid_x + c * CELL_SIZE
            y = grid_y + r * CELL_SIZE
            pygame.draw.rect(screen, GRAY, (x,y, CELL_SIZE, CELL_SIZE))    
    

# Main function
def main():
    global screen  # Use global if screen is modified within functions

    # Get game mode from the main menu
    mode = main_menu()

    # Set AI difficulty based on mode
    if mode == 'normal':
        ai_hard_mode = False
    elif mode == 'hard':
        ai_hard_mode = True

    # Initialize players' boards
    player_board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    ai_board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Player and AI ships
    player_ships = []
    ai_ships = []

    # AI places ships randomly
    place_ships_randomly(ai_board, ai_ships)

    # Player places ships manually
    place_ships_manually(player_board, player_ships)

    # Initialize game variables
    player_turn = True
    ai_targets.clear()  # Clear any previous AI targets
    status_message = ""  # Variable to store status messages

    # Variable to keep track of the winner
    winner = None

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if player_turn:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Check if the click is inside the AI grid
                    if (ai_grid_x <= mouse_x < ai_grid_x + GRID_WIDTH and
                        ai_grid_y <= mouse_y < ai_grid_y + GRID_WIDTH):
                        # Calculate the grid coordinates
                        col = int((mouse_x - ai_grid_x) // CELL_SIZE)
                        row = int((mouse_y - ai_grid_y) // CELL_SIZE)

                        # Check if this cell has already been attacked
                        if ai_board[row][col] in [' ', 'S']:
                            # Player makes a move
                            if ai_board[row][col] == 'S':
                                # It's a hit
                                ai_board[row][col] = 'H'  # "H" for hit
                                # Update the ship's hit count
                                for ship in ai_ships:
                                    if (row, col) in ship.coordinates:
                                        ship.hit()
                                        if ship.is_sunk():
                                            status_message = "You sunk the AI's battleship!"
                                        else:
                                            status_message = "Hit!"
                                        break
                                # Check if all AI ships are sunk
                                if all(ship.is_sunk() for ship in ai_ships):
                                    status_message = "Congratulations! You sunk all the enemy's battleships!"
                                    winner = 'player'
                                    running = False
                            else:
                                # It's a miss
                                ai_board[row][col] = 'M'  # 'M' for miss
                                status_message = "Miss!"
                            player_turn = False  # Switch to AI's turn

        # AI's turn
        if not player_turn and running:
            continue_ai_turn = True  # Control AI's extended turn in Hard Mode
            while continue_ai_turn and running:
                if ai_targets:
                    # AI has targets to pursue
                    row, col = ai_targets.pop()
                else:
                    # AI selects a random cell
                    row = random.randint(0, GRID_SIZE - 1)
                    col = random.randint(0, GRID_SIZE - 1)
                    # Ensure the AI hasn't already attacked this cell
                    while player_board[row][col] in ['H', 'M']:
                        row = random.randint(0, GRID_SIZE - 1)
                        col = random.randint(0, GRID_SIZE - 1)

                # Proceed with attack
                if player_board[row][col] == 'S':
                    # It's a hit
                    player_board[row][col] = 'H'
                    for ship in player_ships:
                        if (row, col) in ship.coordinates:
                            ship.hit()
                            if ship.is_sunk():
                                status_message = "The AI sunk your battleship!"
                            else:
                                status_message = "Your ship was hit!"
                                # Add adjacent cells to ai_targets
                                adjacent_cells = get_adjacent_cells(row, col, player_board)
                                # Avoid duplicates in ai_targets
                                for cell in adjacent_cells:
                                    if cell not in ai_targets:
                                        ai_targets.append(cell)
                            break
                    # Check if all player ships are sunk
                    if all(ship.is_sunk() for ship in player_ships):
                        status_message = 'You have lost the battle, Commander. The enemy has won.'
                        winner = 'ai'
                        running = False
                    if not ai_hard_mode:
                        continue_ai_turn = False  # In Normal Mode, AI makes one move per turn
                else:
                    # It's a miss
                    player_board[row][col] = 'M'
                    status_message = "The AI missed!"
                    continue_ai_turn = False  # AI's turn ends after a miss
            player_turn = True  # Switch back to player's turn

        # Fill the screen with the background image
        # screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        # Create a semi-transparent overlay for the grids
        grid_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay_color = (255, 255, 255, 180)  # RGBA, where A is the alpha value
        grid_overlay.fill(overlay_color)  # Fill the overlay with a semi-transparent color

        # Blit the overlay onto the screen
        screen.blit(grid_overlay, (0, 0))

        # Draw grids onto the screen (over the overlay)
        draw_grid(player_grid_x, player_grid_y, GRID_SIZE, CELL_SIZE)
        draw_grid(ai_grid_x, ai_grid_y, GRID_SIZE, CELL_SIZE)

        # Draw ships on player's grid
        draw_ships(player_ships, player_grid_x, player_grid_y, CELL_SIZE)
        # Draw hits and misses on player's grid
        draw_hits_and_misses(player_board, player_grid_x, player_grid_y, CELL_SIZE)

        # Draw hits and misses on AI's grid
        draw_hits_and_misses(ai_board, ai_grid_x, ai_grid_y, CELL_SIZE)

        # Render the status message
        status_text = FONT_SMALL.render(status_message, True, BLACK)
        status_rect = status_text.get_rect(
            midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10))
        screen.blit(status_text, status_rect)

        # Update the display
        pygame.display.flip()

    # After the game ends, show the Game Over screen
    play_again = game_over_screen(winner)
    if play_again:
        main()  # Restart the game
    else:
        pygame.quit()
        sys.exit()
if __name__ == '__main__':
    main()