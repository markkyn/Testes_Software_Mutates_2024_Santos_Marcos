class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class BaseNumError1(Error):
    """Exception raised for errors in the base number input equals to 1.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    pass


class BaseNumError2(Error):
    """Exception raised for errors in the base number input less than or equals to zero.

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """
    pass


class ArgumentError(Error):
    """Exception raised for errors in the argument number input less than or equals to 0.

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """
    pass


class ZeroError(Error):
    """Exception raised for errors when division by zero.

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """
    pass
