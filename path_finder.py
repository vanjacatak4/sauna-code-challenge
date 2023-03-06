import string
import exceptions


class PathFinder(object):

    START = "@"
    END = "x"
    UP_DOWN = "|"
    LEFT_RIGHT = "-"
    TURN = "+"

    LETTERS = string.ascii_uppercase
    TURN_CHARACTERS = LETTERS + TURN
    UP_DOWN_CHARACTERS = END + TURN_CHARACTERS + UP_DOWN
    LEFT_RIGHT_CHARACTERS = END + TURN_CHARACTERS + LEFT_RIGHT

    ALLOWED_CHARACTERS = TURN_CHARACTERS + "@x-| "

    VERTICAL_DIRECTION = 1
    HORIZONTAL_DIRECTION = 2

    UP = 'UP'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'

    OPPOSITE_DIRECTION = {
        UP: [RIGHT, LEFT],
        DOWN: [RIGHT, LEFT],
        RIGHT: [UP, DOWN],
        LEFT: [UP, DOWN]
    }

    def __init__(self, character_matrix):
        self._character_matrix = self._validate_map(character_matrix)
        self._starting_position = self._find_starting_position()

        self._path = ""
        self._message = ""
        self._solved = False

    def _validate_map(self, character_matrix):
        """Validates the map"""
        start_character_exists = False
        end_character_exists = False
        for row, items in enumerate(character_matrix):
            for col, character in enumerate(items):

                if character == self.START:
                    if not start_character_exists:
                        start_character_exists = True
                        continue

                    raise exceptions.MultipleStartingCharacterException()

                elif character == self.END:
                    end_character_exists = True

                elif character not in self.ALLOWED_CHARACTERS:
                    raise exceptions.InvalidCharacterException()

        # If 'current_position' was not found - missing starting character '@'
        if not start_character_exists:
            raise exceptions.MissingStartingCharacterException()

        # If 'end_character_exists' is False - missing ending character 'x'
        if not end_character_exists:
            raise exceptions.MissingEndingCharacterException()

        return character_matrix

    def _find_starting_position(self):
        for row, items in enumerate(self._character_matrix):
            if self.START in items:
                col = items.index(self.START)
                return row, col

    def _get_neighbors(self, row, col, directions=None):
        """Method for fetching possible moves, based on *directions* input"""
        directions = directions or [self.UP, self.DOWN, self.LEFT, self.RIGHT]
        valid_moves = []
        for direction in directions:

            if direction == self.UP:
                if row > 0 and col < len(self._character_matrix[row - 1]) \
                        and self._character_matrix[row - 1][col] != " ":
                    
                    top_char = self._character_matrix[row - 1][col]

                    if top_char in self.UP_DOWN_CHARACTERS:

                        valid_moves.append([self.UP, (row - 1, col)])

                    elif top_char == self.LEFT_RIGHT \
                                and row > 1 \
                                and col <= len(self._character_matrix[row - 2]) \
                                and self._character_matrix[row - 2][col] in self.UP_DOWN_CHARACTERS:
                            
                            valid_moves.append([self.UP, (row - 2, col)])

            elif direction == self.DOWN:
                if row < len(self._character_matrix) - 1 and col < len(self._character_matrix[row + 1]) \
                        and self._character_matrix[row + 1][col] != " ":
                    
                    bottom_char = self._character_matrix[row + 1][col]

                    if bottom_char in self.UP_DOWN_CHARACTERS:

                        valid_moves.append([self.DOWN, (row + 1, col)])

                    elif bottom_char == self.LEFT_RIGHT \
                                and row < len(self._character_matrix) - 2 \
                                and self._character_matrix[row + 2][col] in self.UP_DOWN_CHARACTERS:
                            
                            valid_moves.append([self.DOWN, (row + 2, col)])

            elif direction == self.LEFT:
                if col > 0 and self._character_matrix[row][col - 1] != " ":

                    left_char = self._character_matrix[row][col - 1]

                    if left_char in self.LEFT_RIGHT_CHARACTERS:

                        valid_moves.append([self.LEFT, (row, col - 1)])

                    elif left_char == self.UP_DOWN \
                                and col > 1 \
                                and self._character_matrix[row][col - 2] in self.LEFT_RIGHT_CHARACTERS:
                            
                            valid_moves.append([self.LEFT, (row, col - 2),])

            elif direction == self.RIGHT:
                if col < len(self._character_matrix[row]) - 1 and self._character_matrix[row][col + 1] != " ":

                    right_char = self._character_matrix[row][col + 1]

                    if right_char in self.LEFT_RIGHT_CHARACTERS:

                        valid_moves.append([self.RIGHT, (row, col + 1)])

                    elif right_char == self.UP_DOWN \
                                and col < len(self._character_matrix[row]) - 2 \
                                and self._character_matrix[row][col + 2] in self.LEFT_RIGHT_CHARACTERS:
                            
                            valid_moves.append([self.RIGHT, (row, col + 2)])

        return valid_moves

    def find_path(self):
        row, col = self._starting_position
        direction = None
        message = []

        while not self._solved:
            character = self._character_matrix[row][col]
            valid_moves = []

            if character in [self.LEFT_RIGHT, self.UP_DOWN]:
                valid_moves = self._get_neighbors(row, col, [direction])

            elif character in self.LETTERS:
                # Keeping direction
                valid_moves = self._get_neighbors(row, col, [direction])
                # If not moves in same directio, check for turn
                if not valid_moves:
                    valid_moves = self._get_neighbors(row, col, self.OPPOSITE_DIRECTION[direction])
                # Character is added with corresponding coordinates
                message.append((character, (row, col)))

            elif character == self.TURN:
                if self._get_neighbors(row, col, [direction]):
                    raise exceptions.FakeTurnException()
                valid_moves = self._get_neighbors(row, col, self.OPPOSITE_DIRECTION[direction])

            elif character == self.START:
                valid_moves = self._get_neighbors(row, col, directions=None)

            elif character == self.END:
                self._solved = True
                self._path = self._path + character
                break

            self._path = self._path + character
            if len(valid_moves) == 1:
                new_direction, (new_row, new_col) = valid_moves[0]
                # If difference between row/col is greater than 1, intersection was crossed - add appropriate char
                if abs(new_row - row) == 2:
                    self._path = self._path + self.LEFT_RIGHT
                elif abs(new_col - col) == 2:
                    self._path = self._path + self.UP_DOWN
                direction, (row, col) = new_direction, (new_row, new_col)
                continue
            elif len(valid_moves) == 0:
                raise exceptions.BrokenPathException
            else:
                raise exceptions.ForkInPathException

        if self._solved:
            # Creates final messages list by removing duplicates and adding only letter from the tuple
            final_message = [item[0] for item in list(dict.fromkeys(message))]
            return self._path, ''.join(final_message)

        return False
