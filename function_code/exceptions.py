class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class BaseNumError1(Error):
    """Exception raised for errors in the base number input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    pass


class BaseNumError2(Error):
    pass


class ArgumentError(Error):
    pass
