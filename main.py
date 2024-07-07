
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colors
BACKGROUND_COLOR = (173, 255, 47)
BUTTON_COLOR =(173, 255, 47)
TEXT_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Font
font = pygame.font.Font(None, 74)

# Game variables
board = [["", "", ""], ["", "", ""], ["", "", ""]]
current_player = "X"
game_over = False

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Function to handle player clicks
def handle_click(x, y):
    row = y // (SCREEN_HEIGHT // 3)
    col = x // (SCREEN_WIDTH // 3)
    if board[row][col] == "":
        board[row][col] = current_player
        return True
    return False

# Function to check for a winner
def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    
    # Check for draw
    for row in board:
        if "" in row:
            return None
    return "Draw"

# Function to switch players
def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Function to draw the game board
def draw_board():
    screen.fill(BACKGROUND_COLOR)
    for x in range(1, 3):
        pygame.draw.line(screen, TEXT_COLOR, (SCREEN_WIDTH // 3 * x, 0), (SCREEN_WIDTH // 3 * x, SCREEN_HEIGHT), 5)
        pygame.draw.line(screen, TEXT_COLOR, (0, SCREEN_HEIGHT // 3 * x), (SCREEN_WIDTH, SCREEN_HEIGHT // 3 * x), 5)
    
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                draw_text(board[row][col], font, TEXT_COLOR, screen, (col * SCREEN_WIDTH // 3) + SCREEN_WIDTH // 6, (row * SCREEN_HEIGHT // 3) + SCREEN_HEIGHT // 6)

# Function to restart the game
def restart_game():
    global board, current_player, game_over
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    current_player = "X"
    game_over = False

# Main game loop
def game_loop():
    global game_over
    running = True
    while running:
        draw_board()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if handle_click(event.pos[0], event.pos[1]):
                    winner = check_winner()
                    if winner:
                        game_over = True
                        results_screen(winner)
                    else:
                        switch_player()
        
        pygame.display.update()

# Results screen
def results_screen(winner):
    result_shown = True
    while result_shown:
        screen.fill(BACKGROUND_COLOR)
        
        if winner == "Draw":
            draw_text('It\'s a Draw!!!', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        else:
            draw_text(f'{winner} is the Winner!!!', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        
        main_menu_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 60, 200, 50)
        
        pygame.draw.rect(screen, BUTTON_COLOR, main_menu_button)
        pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
        
        draw_text('Main Menu', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        draw_text('Restart', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 85)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.collidepoint(event.pos):
                    main_menu()
                if restart_button.collidepoint(event.pos):
                    restart_game()
                    game_loop()
        
        pygame.display.update()

# Placeholder functions for the other menus
def pause_menu():
    paused = True
    while paused:
        screen.fill(BACKGROUND_COLOR)
        
        draw_text('Paused', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        
        continue_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50)
        exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        
        pygame.draw.rect(screen, BUTTON_COLOR, continue_button)
        pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        
        draw_text('Continue', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25)
        draw_text('Exit', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(event.pos):
                    paused = False
                if exit_button.collidepoint(event.pos):
                    main_menu()
        
        pygame.display.update()

def options_menu():
    options_running = True
    while options_running:
        screen.fill(BACKGROUND_COLOR)
        
        draw_text('Options', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        
        sound_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50)
        main_menu_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        
        pygame.draw.rect(screen, BUTTON_COLOR, sound_button)
        pygame.draw.rect(screen, BUTTON_COLOR, main_menu_button)
        
        draw_text('Sound: On/Off', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25)
        draw_text('Main Menu', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sound_button.collidepoint(event.pos):
                    # Toggle sound logic here
                    pass
                if main_menu_button.collidepoint(event.pos):
                    options_running = False
                    main_menu()
        
        pygame.display.update()

def appearance_menu():
    appearance_running = True
    while appearance_running:
        screen.fill(BACKGROUND_COLOR)
        
        draw_text('Appearance', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        
        # Add buttons for appearance options
        main_menu_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        
        pygame.draw.rect(screen, BUTTON_COLOR, main_menu_button)
        
        draw_text('Main Menu', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.collidepoint(event.pos):
                    appearance_running = False
                    main_menu()
        
        pygame.display.update()

def game_setup_screen():
    setup_running = True
    while setup_running:
        screen.fill(BACKGROUND_COLOR)
        
        draw_text('How many times you want to play:', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        
        # Add input field and buttons for game setup
        start_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50)
        back_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        
        pygame.draw.rect(screen, BUTTON_COLOR, start_button)
        pygame.draw.rect(screen, BUTTON_COLOR, back_button)
        
        draw_text('Start', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25)
        draw_text('Go Back', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    setup_running = False
                    restart_game()
                    game_loop()
                if back_button.collidepoint(event.pos):
                    setup_running = False
                    main_menu()
        
        pygame.display.update()

def main_menu():
    menu_running = True
    while menu_running:
        screen.fill(BACKGROUND_COLOR)
        
        draw_text('Tic Tac Toe', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        
        play_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100, 200, 50)
        options_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50)
        appearance_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        
        pygame.draw.rect(screen, BUTTON_COLOR, play_button)
        pygame.draw.rect(screen, BUTTON_COLOR, options_button)
        pygame.draw.rect(screen, BUTTON_COLOR, appearance_button)
        
        draw_text('Play', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 75)
        draw_text('Options', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25)
        draw_text('Appearance', font, TEXT_COLOR, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    menu_running = False
                    game_setup_screen()
                if options_button.collidepoint(event.pos):
                    menu_running = False
                    options_menu()
                if appearance_button.collidepoint(event.pos):
                    menu_running = False
                    appearance_menu()
        
        pygame.display.update()

# Start the main menu
main_menu()
