from llama_index.llms import ollama as ol
from llama_index.core import Settings
from .LlmPlaceholder import LlmPlaceholder


class ModelOllama(LlmPlaceholder):
    """This class serves as an object for instances of ollama models."""

    def __init__(self,
                 api_key,
                 model,
                 temperature,
                 max_tokens,
                 timeout
                 ):
        super().__init__(
            api_key,
            model,
            temperature,
            max_tokens
        )
        self.llm_model = Settings
        self.llm_model.llm = ol.Ollama(model=model, temperature=temperature,request_timeout=timeout)

    def ask_model(self, chat):
        resp = self.llm_model.llm.complete(chat)
        return resp

    def get_model(self):
        return self.model
