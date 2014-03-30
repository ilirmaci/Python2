# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        '''(Rat, str, int, int) -> NoneType

        Create a Rat object with attributes symbol, row, col,
        and num_sprouts_eaten (set at 0).
        Preconditions: len(symbol) == 1, row >= 1, col >= 1
        
        >>> paul = Rat('P', 1, 4)
        >>> paul.symbol
        'P'
        >>> paul.row
        1
        >>> paul.col
        4
        >>> paul.num_sprouts_eaten
        0
        '''
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def __str__(self):
        '''(Rat) -> str

        Return str showing rat symbol, position, and sprouts eaten
        in format: symbol at (row, col) ate num_sprouts_eaten sprouts.
        
        >>> paul = Rat('P', 1, 4)
        >>> paul.eat_sprout()
        >>> print(paul)
        P at (1, 4) ate 1 sprouts.
        '''
        return '{0} at ({1}, {2}) ate {3} sprouts.'\
               .format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
            

    def set_location(self, row, col):
        '''(Rat, int, int) -> NoneType

        Set self position to row and col.
        Preconditions: row >= 1, col >= 1
        
        >>> paul = Rat('P', 1, 4)
        >>> paul.set_location(2, 4)
        >>> paul.row
        2
        >>> paul.col
        4
        '''
        self.row = row
        self.col = col

    def eat_sprout(self):
        '''(Rat) -> NoneType

        Increment rat's num_sprouts_eaten attribute.
        
        >>> paul = Rat('P', 1, 4)
        >>> paul.num_sprouts_eaten
        0
        >>> paul.eat_sprout()
        >>> paul.num_sprouts_eaten
        1
        '''

        self.num_sprouts_eaten += 1
        
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        '''(Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize Maze with two rats.
        Preconditions: lists of maze must be of equal length and
        start/end with WALL. First and last list of maze must be
        entirely made of WALL. rat_1 and rat_2 positions must refer
        to valid HALL positions within maze.
        
        >>> lab = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                        ['#', '.', '.', '.', '.', '.', '#'],\
                        ['#', '.', '#', '#', '#', '.', '#'],\
                        ['#', '.', '.', '@', '#', '.', '#'],\
                        ['#', '@', '#', '.', '@', '.', '#'],\
                        ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> lab.maze[1]
        ['#', '.', '.', '.', '.', '.', '#']
        >>> print(lab.rat_1)
        J at (1, 1) ate 0 sprouts.
        >>> print(lab.rat_2)
        P at (1, 4) ate 0 sprouts.
        >>> lab.num_sprouts_left
        3
        '''
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        # count occurrences of SPROUT in all rows of maze
        num_sprouts_left = 0 
        for i in range(len(maze)):
            num_sprouts_left += maze[i].count(SPROUT)

        self.num_sprouts_left = num_sprouts_left

    def __str__(self):
        '''(Maze) -> str
        Return str with maze and status of each rat.

        >>> lab = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                        ['#', '.', '.', '.', '.', '.', '#'],\
                        ['#', '.', '#', '#', '#', '.', '#'],\
                        ['#', '.', '.', '@', '#', '.', '#'],\
                        ['#', '@', '#', '.', '@', '.', '#'],\
                        ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> print(lab)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        '''
        s = ''  #accummulator string

        # extract maze and place rat symbols in it
        m = self.maze
        m[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        m[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

        # adding maze matrix
        for i in range(len(m)):
            for j in range(len(m[i])):
                s = s + m[i][j]
            s = s + '\n'

        # adding rats
        s = s + str(self.rat_1) + '\n' + str(self.rat_2)
        return s

    def is_wall(self, row, col):
        '''(Maze, int, int) -> bool

        Return if there is a WALL at given row and col of maze.
        Preconditions: row < len(self.maze), col < len(self.maze[0])
        
        >>> lab = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                        ['#', '.', '.', '.', '.', '.', '#'],\
                        ['#', '.', '#', '#', '#', '.', '#'],\
                        ['#', '.', '.', '@', '#', '.', '#'],\
                        ['#', '@', '#', '.', '@', '.', '#'],\
                        ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> lab.is_wall(0, 0)
        True
        >>> lab.is_wall(1, 1)
        False
        >>> lab.is_wall(4, 1)
        False
        '''
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        '''(Maze, int, int) -> str

        Return character indexed by row and col in maze. If a rat
        is present at that position, return rat's symbol.
        Precondition: row < len(self.maze), col < len(self.maze[0])
        
        >>> lab = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                        ['#', '.', '.', '.', '.', '.', '#'],\
                        ['#', '.', '#', '#', '#', '.', '#'],\
                        ['#', '.', '.', '@', '#', '.', '#'],\
                        ['#', '@', '#', '.', '@', '.', '#'],\
                        ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> lab.get_character(0, 0)
        '#'
        >>> lab.get_character(1, 2)
        '.'
        >>> lab.get_character(1, 1)
        'J'
        >>> lab.get_character(3, 3)
        '@'
        '''
        if (self.rat_1.row, self.rat_1.col) == (row, col):
            return self.rat_1.symbol
        if (self.rat_2.row, self.rat_2.col) == (row, col):
            return self.rat_2.symbol

        return self.maze[row][col]

    def move(self, rat, row_move, col_move):
        '''(Maze, Rat, int, int) -> bool

        Iff new position is not WALL, move rat from current position as specified
        by row_move and col_move and return True. If new position is SPROUT, have
        rat eat it and change rat location to HALL.
        Preconditions: row_move is UP, NO_CHANGE, or DOWN. col_move is LEFT, NO_CHANGE,
        or RIGHT.

        >>> lab = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                        ['#', '.', '.', '.', '.', '.', '#'],\
                        ['#', '.', '#', '#', '#', '.', '#'],\
                        ['#', '.', '.', '@', '#', '.', '#'],\
                        ['#', '@', '#', '.', '@', '.', '#'],\
                        ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> lab.move(lab.rat_1, NO_CHANGE, NO_CHANGE)
        True
        >>> print(lab.rat_1)
        J at (1, 1) ate 0 sprouts.
        >>> lab.move(lab.rat_1, DOWN, NO_CHANGE)
        True
        >>> print(lab.rat_1)
        J at (2, 1) ate 0 sprouts.
        >>> lab.move(lab.rat_1, DOWN, RIGHT)
        True
        >>> lab.move(lab.rat_1, NO_CHANGE, RIGHT)
        True
        >>> print(lab.rat_1)
        J at (3, 3) ate 1 sprouts.
        >>> lab.move(lab.rat_1, NO_CHANGE, LEFT)
        True
        >>> lab.get_character(3, 3)
        '.'
        >>> lab.move(lab.rat_2, DOWN, NO_CHANGE)
        False
        >>> print(lab.rat_2)
        P at (1, 4) ate 0 sprouts.
        '''
        # get rat position
        old_row = rat.row
        old_col = rat.col

        # get desired position
        new_row = old_row + row_move
        new_col = old_col + col_move

        # get target location character
        target = self.get_character(new_row, new_col)

        # stop with False if desired position is WALL
        if target == WALL:
            return False
        # process new position
        if target == HALL:
            rat.set_location(new_row, new_col) #move rat
        elif target == SPROUT:
            rat.set_location(new_row, new_col) #move rat
            rat.eat_sprout()                   #have rat eat sprout
            self.num_sprouts_left -= 1         #decrease sprout count
            self.maze[new_row][new_col] = HALL #change tile to HALL
        return True
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
