from transformers import AutoModelForCausalLM, AutoTokenizer

from open_code_gen_api.logger import logger


class CodeGenModel:
    pass


class SalesforceCodeGen(CodeGenModel):
    def _tokenize(self, input: str):
        return self.tokenizer(input, return_tensors="pt").input_ids

    def _decode(self, sample: str):
        return self.tokenizer.decode(sample[0], skip_special_tokens=True)

    def infer(self, input: str):
        logger.info("Tokenizing... %s", input)
        inputs = self._tokenize(input)
        logger.info("Generating... ")
        sample = self.model.generate(inputs, max_length=128)
        logger.info("Decoding...")
        return self._decode(sample)


class SalesforceCodeGen350M(SalesforceCodeGen):
    def __init__(self) -> None:
        super().__init__()
        logger.info("Loading model...")
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
        self.model = AutoModelForCausalLM.from_pretrained(
            "Salesforce/codegen-350M-mono"
        )


class SalesforceCodeGen2B(SalesforceCodeGen):
    def __init__(self) -> None:
        super().__init__()
        logger.info("Loading model...")
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-mono")
        self.model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-mono")
