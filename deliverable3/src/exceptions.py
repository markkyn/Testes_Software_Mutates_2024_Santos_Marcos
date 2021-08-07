class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class BaseNumError1(Error):
    """Exception raised for errors in the base number input equals to 1."""
    pass


class BaseNumError2(Error):
    """Exception raised for errors in the base number input less than or equals to zero."""
    pass


class ArgumentError(Error):
    """Exception raised for errors in the argument number input less than or equals to 0."""
    pass


class ZeroError(Error):
    """Exception raised for errors when division by zero."""
    pass
