import pygame
from board.RenderBoard import render_board

# Setup to draw screen
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

# Setup window customization
pygame.display.set_caption("PyChess")
pygame.display.set_icon(pygame.image.load("assets/chess_icon.png"))


# Run game loop
while running:

    # Exit window when 'X' is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Wipe screen to draw next frame
    render_board(screen)

    # Prints work to the screen
    pygame.display.flip()

    # Set fps for screen drawing
    clock.tick(24)

pygame.quit()
