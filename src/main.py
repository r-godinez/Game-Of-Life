import pygame
import sys
from simulation import Simulation

# Initialize Pygame
pygame.init()

# Color and Window Constants
GREY = (29, 29, 29)  # Background color
WINDOW_WIDTH = 750    # Width of the simulation window
WINDOW_HEIGHT = 750   # Height of the simulation window
CELL_SIZE = 25       # Size of each cell in the grid
FPS = 12             # Frames per second for the simulation

# Create the simulation window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")  # Set the window title

# Create a clock to manage frame rate
clock = pygame.time.Clock()

# Initialize the simulation object
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the window is closed
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle cell state when mouse is clicked
            pos = pygame.mouse.get_pos()  # Get the mouse position
            row = pos[1] // CELL_SIZE      # Calculate row index
            column = pos[0] // CELL_SIZE   # Calculate column index
            simulation.toggle_cell(row, column)  # Toggle the cell's state
        if event.type == pygame.KEYDOWN:
            # Start the simulation when Enter key is pressed
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life is running")  # Update window title
            # Stop the simulation when Space key is pressed
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life has stopped")  # Update window title
            # Increase FPS when 'F' key is pressed
            elif event.key == pygame.K_f:
                FPS += 2
            # Decrease FPS when 'S' key is pressed, ensuring it doesn't go below 5
            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2
            # Create a random state when 'R' key is pressed
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            # Clear the grid when 'C' key is pressed
            elif event.key == pygame.K_c:
                simulation.clear()

    # 2. Updating State
    simulation.update()  # Update the simulation state

    # 3. Drawing
    window.fill(GREY)        # Fill the window with the background color
    simulation.draw(window)  # Draw the current state of the simulation

    pygame.display.update()  # Update the display
    clock.tick(FPS)         # Control the frame rate
