
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Simple Pygame")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Player properties
player_x = 50
player_y = screen_height // 2
player_speed = 5
player_size = 50

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player within screen bounds
    player_x = max(0, min(player_x, screen_width - player_size))
    player_y = max(0, min(player_y, screen_height - player_size))

    # Drawing
    screen.fill(white)  # Clear screen with white
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size)) # Draw red square for player

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()