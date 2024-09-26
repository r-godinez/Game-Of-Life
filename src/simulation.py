from grid import Grid

class Simulation:
    """
    A class to simulate a grid-based environment using a Grid object.
    This simulation supports toggling cells, updating states based on neighbor counts,
    and starting/stopping the simulation.

    Attributes:
        grid (Grid): The main grid representing the simulation state.
        temp_grid (Grid): A temporary grid for storing state updates.
        rows (int): The number of rows in the grid.
        columns (int): The number of columns in the grid.
        run (bool): A flag indicating whether the simulation is currently running.
    """

    def __init__(self, width, height, cell_size):
        """
        Initializes the Simulation with the specified grid dimensions and cell size.

        Args:
            width (int): The total width of the simulation grid.
            height (int): The total height of the simulation grid.
            cell_size (int): The size of each cell in the grid.
        """
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.run = False

    def draw(self, window):
        """
        Draws the current state of the grid onto the specified window.

        Args:
            window: The window or surface to draw the grid onto.
        """
        self.grid.draw(window)

    def count_live_neighbors(self, grid, row, column):
        """
        Counts the number of live neighbors for a specific cell in the grid.

        Args:
            grid (Grid): The grid to check for live neighbors.
            row (int): The row index of the cell.
            column (int): The column index of the cell.

        Returns:
            int: The count of live neighbors surrounding the specified cell.
        """
        live_neighbors = 0

        # Neighbor offsets represent the relative positions of neighbors
        neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1),
                            (0, -1),          (0, 1),
                            (1, -1), (1, 0), (1, 1)]
        for offset in neighbor_offsets:
            # Calculate new row and column with wrapping around the grid
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1:  # Cell is alive
                live_neighbors += 1

        return live_neighbors

    def update(self):
        """
        Updates the grid state based on the current configuration of live cells.
        The function applies the rules of the simulation and modifies the temp_grid.
        If the simulation is running, it will update the cells based on their neighbors.
        """
        if self.is_running():
            for row in range(self.rows):
                for column in range(self.columns):
                    live_neighbors = self.count_live_neighbors(self.grid, row, column)
                    cell_value = self.grid.cells[row][column]

                    # Apply the rules of the simulation
                    if cell_value == 1:  # Cell is alive
                        if live_neighbors > 3 or live_neighbors < 2:
                            self.temp_grid.cells[row][column] = 0  # Cell dies
                        else:
                            self.temp_grid.cells[row][column] = 1  # Cell stays alive
                    else:  # Cell is dead
                        if live_neighbors == 3:
                            self.temp_grid.cells[row][column] = 1  # Cell becomes alive
                        else:
                            self.temp_grid.cells[row][column] = 0  # Cell stays dead

            # Update the main grid with the temporary grid's state
            for row in range(self.rows):
                for column in range(self.columns):
                    self.grid.cells[row][column] = self.temp_grid.cells[row][column]

    def is_running(self):
        """
        Checks whether the simulation is currently running.

        Returns:
            bool: True if the simulation is running, False otherwise.
        """
        return self.run

    def start(self):
        """
        Starts the simulation, setting the run flag to True.
        """
        self.run = True

    def stop(self):
        """
        Stops the simulation, setting the run flag to False.
        """
        self.run = False

    def clear(self):
        """
        Clears the grid if the simulation is not running.
        This resets all cells to the dead state.
        """
        if not self.is_running():
            self.grid.clear()

    def create_random_state(self):
        """
        Fills the grid with a random state if the simulation is not running.
        Cells will be randomly set to alive or dead.
        """
        if not self.is_running():
            self.grid.fill_random()

    def toggle_cell(self, row, column):
        """
        Toggles the state of a specific cell between alive and dead.

        Args:
            row (int): The row index of the cell to toggle.
            column (int): The column index of the cell to toggle.
        """
        if not self.is_running():
            self.grid.toggle_cell(row, column)
