import pydantic


class PromptRequest(pydantic.BaseModel):
    prompt_text: str
