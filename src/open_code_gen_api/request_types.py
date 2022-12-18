"""Defines request types for the API."""

import pydantic


# pylint: disable=no-member, too-few-public-methods
class PromptRequest(pydantic.BaseModel):
    """Request model for requesting a prompt."""

    prompt_text: str
    max_response_length: int = 128
