"""Defines the model services that can provide code generation.
At the moment, fully based in the HuggingFace Transformers library.
"""
from transformers import AutoModelForCausalLM, AutoTokenizer  # type: ignore

from open_code_gen_api.logger import logger

# pylint: disable=too-few-public-methods


class CodeGenModel:
    """Base abstract class Model"""

    MAX_LENGTH = 2048

    def infer(self, input_: str) -> str:
        """Abstract infer method, takes a text prompt and returns the model response."""
        raise NotImplementedError("Abstract method")


class SalesforceCodeGen(CodeGenModel):
    """Base Salesforce CodeGen class.

    Defines the behavior but does not instruct how to load the model.
    """

    def __init__(self) -> None:
        super().__init__()
        self.tokenizer: AutoTokenizer = None
        self.model: AutoModelForCausalLM = None
        raise NotImplementedError(
            "This is an abstract class, cannot be instantiated directly"
        )

    def _tokenize(self, input_: str):
        # pylint: disable-next=not-callable
        return self.tokenizer(input_, return_tensors="pt").input_ids

    def _decode(self, sample: str):
        return self.tokenizer.decode(sample[0], skip_special_tokens=True)

    def infer(self, input_: str):
        """Infer method, takes a text prompt and returns the model response."""
        logger.info("Tokenizing... %s", input_)
        inputs = self._tokenize(input_)
        logger.info("Generating... ")
        sample = self.model.generate(inputs, max_length=CodeGenModel.MAX_LENGTH)
        logger.info("Decoding...")
        return self._decode(sample)


class SalesforceCodeGen350M(SalesforceCodeGen):
    """Loads the 350M parameters mono (Python only) model."""

    def __init__(self) -> None:
        super().__init__()
        logger.info("Loading model...")
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
        self.model = AutoModelForCausalLM.from_pretrained(
            "Salesforce/codegen-350M-mono"
        )


class SalesforceCodeGen2B(SalesforceCodeGen):
    """Loads the 2B parameters mono (Python only) model."""

    def __init__(self) -> None:
        super().__init__()
        logger.info("Loading model...")
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-mono")
        self.model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-mono")
