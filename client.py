from client_options import ClientOptions
from enhance_options import EnhanceOptions

class Client:
    """
    Client for interacting with the AI Acoustics API.
    """
    def __init__(self, client_options: ClientOptions):
        self.options = client_options

    def enhance_file(self, input: str, output: str, options: EnhanceOptions):
        """
        Enhances an audio file based on provided options.
        
        :param input: Input file path or URI.
        :param output: Output file path or URI.
        :param options: Enhancement options.
        """
        print(f"Enhancing file from {input} to {output} with options: {options.__dict__}")
