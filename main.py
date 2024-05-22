import pygame

# Setup to draw screen
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True


# Run game loop
while running:

    # Exit window when 'X' is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Wipe screen to draw next frame
    screen.fill("darkgrey")

    # Prints work to the screen
    pygame.display.flip()

    # Set fps for screen drawing
    clock.tick(24)

pygame.quit()
