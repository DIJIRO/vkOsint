class ClientError(SystemExit):

    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class ProxyError(ClientError):
    """Sorry, there was a problem with your request"""

class WrongAuthCredientals(ClientError):
    """Wrong username or password"""

class JsonDecodeError(ClientError):
    """Error in decoding json response"""

class LimitError(ClientError):
    """Requests limist reached"""

class FloodError(ClientError):
    """Flood control triggerred"""

class TokenError(ClientError):
    """Requests limist reached"""

class UnknownError(ClientError):
    """Unknown Error"""

