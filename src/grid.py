import pygame
import random

class Grid:
    """
    A class to represent a grid for the simulation.

    Attributes:
        rows (int): The number of rows in the grid.
        columns (int): The number of columns in the grid.
        cell_size (int): The size of each cell in the grid.
        cells (list of list of int): A 2D list representing the state of each cell (0 for dead, 1 for alive).
    """

    def __init__(self, width, height, cell_size):
        """
        Initializes the Grid with the specified dimensions and cell size.

        Args:
            width (int): The total width of the grid.
            height (int): The total height of the grid.
            cell_size (int): The size of each cell in the grid.
        """
        self.rows = height // cell_size  # Calculate the number of rows
        self.columns = width // cell_size  # Calculate the number of columns
        self.cell_size = cell_size  # Store the size of each cell
        # Initialize the grid with dead cells (0)
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        """
        Draws the current state of the grid onto the specified window.

        Args:
            window: The window or surface to draw the grid onto.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                # Set the color based on cell state: green for alive, dark grey for dead
                color = (0, 255, 0) if self.cells[row][column] else (55, 55, 55)
                # Draw the cell rectangle on the window
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def fill_random(self):
        """
        Fills the grid with a random state, where each cell has a 25% chance of being alive.
        This simulates a random distribution of live (1) and dead (0) cells.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                # Randomly set each cell to be alive (1) or dead (0)
                self.cells[row][column] = random.choice([1, 0, 0, 0])  # 1 in 4 chance of being alive

    def clear(self):
        """
        Clears the grid by setting all cells to dead (0).
        """
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0  # Set each cell to dead

    def toggle_cell(self, row, column):
        """
        Toggles the state of a specific cell between alive (1) and dead (0).

        Args:
            row (int): The row index of the cell to toggle.
            column (int): The column index of the cell to toggle.
        """
        if 0 <= row < self.rows and 0 <= column < self.columns:
            # Toggle the cell's state (from 0 to 1 or from 1 to 0)
            self.cells[row][column] = not self.cells[row][column]
