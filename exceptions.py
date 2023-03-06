class PathFinderException(Exception):
    """Base PathFinder exception"""

    def __init__(self, message=None):
        self.message = message or "PathFinderException"
        super().__init__(self.message)


class InvalidCharacterException(PathFinderException):
    """Invalid Character Exception

    Attributes:
        message - explanation of the error
    """

    def __init__(self, message="Invalid character found in map"):
        self.message = message
        super().__init__(self.message)


class MissingStartingCharacterException(PathFinderException):
    """Exception raised if starting character cannot be found.

    Attributes:
        message - explanation of the error
    """

    def __init__(self, message="Map is missing starting character '@'"):
        self.message = message
        super().__init__(self.message)


class MissingEndingCharacterException(PathFinderException):
    """Exception raised ending character cannot be found

    Attributes:
        message - explanation of the error
    """

    def __init__(self, message="Map is missing ending character 'x'"):
        self.message = message
        super().__init__(self.message)


class MultipleStartingCharacterException(PathFinderException):
    """Exception raised when multiple starting characters are found

    Attribute:
        message - explanation of the error
    """

    def __init__(self, message="Map has multiple starting characters '@'"):
        self.message = message
        super().__init__(self.message)


class BrokenPathException(PathFinderException):
    """Exception raised when PathFinder gets no valid next moves

    Attributes:
        message - explanation of the error
    """

    def __init__(self, message="Map has broken path"):
        self.message = message
        super().__init__(self.message)


class ForkInPathException(PathFinderException):
    """Exception raised when PathFinder object finds more than one possible next moves

    Attributes:
        message - explanation of the error
    """

    def __init__(self, message="Map has Fork in Path"):
        self.message = message
        super().__init__(self.message)


class FakeTurnException(PathFinderException):
    """Exception raised when PathFinder finds turn character '+', but path continues in the same direction

    Attributes:
        message - explanation of the error
    """

    def __init__(self, message="Map has Fake Turn"):
        self.message = message
        super().__init__(self.message)
