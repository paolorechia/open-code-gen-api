from open_code_gen_api.logger import logger
from open_code_gen_api.open_code_gen_model.model_service import SalesforceCodeGen350M


def cli(prompt: str):
    logger.info("CLI called with prompt: %s", prompt)
    model = SalesforceCodeGen350M()
    result = model.infer(prompt)
    logger.info("Result: %s", result)
    return result
