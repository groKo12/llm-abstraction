
class LlmPlaceholder():
    """This class servers as an abstraction layer for a variety of LLMs"""

    def __init__(self,
                 api_key,
                 model,
                 temperature,
                 max_tokens
                 ):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def ask_model(self, chat):
        pass

    @property
    def get_model(self):
        pass

