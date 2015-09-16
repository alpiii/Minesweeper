"""
Minesweeper Game
developed with python
"""

import random


class Cell(object):
    """
    This class contains properties of a cell object.
    Each cell has a row and column value.
    Value is the count of the cells which are neighbours of this cell contain bombs
    """

    is_open = False
    value = 0

    def __init__(self, row, column):
        self.row = row
        self.column = column


class MineSweeper(object):
    """
    Game class with game controls and operations.
    """

    row_size = 0
    column_size = 0
    bomb_count = 0
    cells = []

    # Initialize game
    def __init__(self, row, column, difficulty):

        self.row_size = row
        self.column_size = column
        for i in range(1, (column + 1)):
            for j in range(1, (row + 1)):
                self.cells.append(Cell(i, j))
        if difficulty == "Easy":
            if row * column < 30:
                self.bomb_count = 5
            elif row * column < 100:
                self.bomb_count = 10
            else:
                self.bomb_count = 15
        elif difficulty == "Medium":
            if row * column < 30:
                self.bomb_count = 10
            elif row * column < 100:
                self.bomb_count = 15
            else:
                self.bomb_count = 20
        elif difficulty == "Hard":
            if row * column < 30:
                self.bomb_count = 15
            elif row * column < 100:
                self.bomb_count = 20
            else:
                self.bomb_count = 30
        else:
            raise Exception("Your level input is wrong!")

    def game_over_control(self):
        """
        Detects if the game is over or not.
        If closed cell count is equal to the bomb count, player wins.
        :return:True if player wins. False if the game continues.
        """
        count = 0
        for cell in self.cells:
            if cell.is_open is False:
                count += 1
        if count == self.bomb_count:
            return True
        else:
            return False

    def game_flow(self):
        """
        Controls the main game flow
        :return: None
        """
        game_end = False
        score = 04
        self.print_field()
        while game_end is False:
            print "\n"
            print "Choose row and then column (Example: 5 4): "
            user_row, user_column = int(raw_input()), int(raw_input())
            if self.cells[self.row_size * (user_row - 1) + (user_column - 1)].is_open is False:
                if self.cells[self.row_size * (user_row - 1) + (user_column - 1)].value == 99:
                    game_end = True
                    print "\n"
                    print "Bomb! Game is over"
                    print "Your score is: %r" % score
                    self.open_field()
                else:
                    self.cells[self.row_size * (user_row - 1) + (user_column - 1)].is_open = True
                    score += 5
                    if self.game_over_control() is False:
                        self.print_field()
                    else:
                        game_end = True
                        print "\n"
                        print "Congratulations! You win!"
                        print "Your score is: %r" % score
                        self.open_field()

    def print_field(self):
        """
        Prints the cells to the screen.
        :return: None
        """
        print ("\n"),
        for index, cell in enumerate(self.cells):
            if index % self.row_size is 0:
                print ("\n"),
            if cell.is_open is True:
                print ("%s \t" % cell.value),
            else:
                print "X \t",

    def open_field(self):
        """
        Opens all of the cells' values and prints them to the console.
        :return: None
        """
        for index, cell in enumerate(self.cells):
            if index % self.row_size is 0:
                print ("\n"),
            print ("%s \t" % cell.value),
        print "\n"

    def insert_mines(self):
        """
        Insert specified number of mines into the area, increase values of its neighbour cells.
        :return: None
        """
        bomb_position = random.sample(range(0, (self.row_size * self.column_size) - 1),
                                      self.bomb_count)
        for bomb in bomb_position:
            self.cells[int(bomb)].value = 99
        for located_bomb in bomb_position:
            neighbour_list = []
            # except right corner
            if (located_bomb+1) % self.row_size != 0:
                neighbour_list.append(located_bomb+1)
                neighbour_list.append(located_bomb+self.row_size+1)
                neighbour_list.append(located_bomb-self.row_size+1)
            # except left corner
            if located_bomb % self.row_size != 0:
                neighbour_list.append(located_bomb-1)
                neighbour_list.append(located_bomb+self.row_size-1)
                neighbour_list.append(located_bomb-self.row_size-1)
            # all fields
            neighbour_list.append(located_bomb+self.row_size)
            neighbour_list.append(located_bomb-self.row_size)
            # increase proper neighbours one
            for neighbour in neighbour_list:
                if -1 < neighbour < len(self.cells):
                    if self.cells[neighbour].value != 99:
                        self.cells[neighbour].value += 1


# Testing
if __name__ == "__main__":
    print "Welcome to minesweeper game!"
    print "Enter column number: "
    ROW_NUMBER = int(raw_input())
    print "Enter row number: "
    COLUMN_NUMBER = int(raw_input())
    print "Choose your level: Easy / Medium / Hard "
    DIFFICULTY_LEVEL = raw_input()
    try:
        GAME = MineSweeper(ROW_NUMBER, COLUMN_NUMBER, DIFFICULTY_LEVEL)
        GAME.insert_mines()
        GAME.game_flow()
    except Exception as exc:
        print exc
