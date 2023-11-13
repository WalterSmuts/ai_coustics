class EnhanceOptions:
    """
    Options for audio enhancement.
    """
    def __init__(self, options: dict):
        self.loudness = options.get("loudness", {})
        self.noise = options.get("noise", {})
