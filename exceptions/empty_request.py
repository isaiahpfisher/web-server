class EmptyRequestException(Exception):
    """Exception raised for an empty request."""

    def __init__(self, message="Empty request"):
        self.message = message
        super().__init__(self.message)
