"""Model to test the model locally, using the terminal."""
from open_code_gen_api.logger import logger
from open_code_gen_api.open_code_gen_model.model_service import SalesforceCodeGen350M


def cli(prompt: str):
    """Loads the model, passes a prompt through it and returns the reuslt."""
    logger.info("CLI called with prompt: %s", prompt)
    model = SalesforceCodeGen350M()
    model_result = model.infer(prompt)
    logger.info("Result: %s", model_result)
    return model_result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        sys.exit(f"Usage: {sys.argv[0]} <prompt>")

    result = cli(" ".join(sys.argv[1:]))
    print(result)
