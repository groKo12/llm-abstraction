from .LlmPlaceholder import LlmPlaceholder
from llama_index.llms.gemini import Gemini


class ModelGemini(LlmPlaceholder):
    """This instantiates an object of the Gemini Model Class."""

    def __init__(self,
                 api_key,
                 model,
                 temperature,
                 max_tokens
                 ):
        # Inherit LlmPlaceholder class data
        super().__init__(
            api_key,
            model,
            temperature,
            max_tokens
        )

    def ask_model(self, chat):
        query = Gemini(api_key=self.api_key,
                       model=self.model,
                       temperature=self.temperature,
                       max_tokens=self.max_tokens
                       )
        query_answer = query.complete(chat)
        return query_answer

    def get_model(self):
        return self.model
