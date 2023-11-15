class ClientOptions:
    """
    Configuration options for the AI Acoustics client.
    """
    def __init__(self, options: dict):
        self.host = options.get("host")
        self.token = options.get("token")
