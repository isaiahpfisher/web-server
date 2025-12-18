class ForbiddenException(Exception):
    """Exception raised for a forbidden request."""

    def __init__(self, code=403, message="Forbidden"):
        self.message = message
        self.code = code
        super().__init__(self.message)
