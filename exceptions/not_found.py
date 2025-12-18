class NotFoundException(Exception):
    """Exception raised for a not found error."""

    def __init__(self, code=404, message="Not Found"):
        self.message = message
        self.code = code
        super().__init__(self.message)
