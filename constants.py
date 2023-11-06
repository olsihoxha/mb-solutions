from enum import Enum

JOB_NAME = 'qa_search'

OPEN_AI_API_KEY = 'key'

HUGGING_FACE_API_KEY = 'key'

LOGO_IMG = 'https://www.pngmart.com/files/22/Mercedes-Benz-Logo-PNG-Isolated-File.png'


class EmbeddingType(str, Enum):
    OPEN_AI = 'openai'
    HUGGING_FACE = 'hugging_face'


class LlmType(str, Enum):
    OPEN_AI_LLM = 'openai_llm'
    FALCON_LLM = 'falcon_llm'
