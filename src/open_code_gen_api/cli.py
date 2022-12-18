from open_code_gen_api.logger import logger
from open_code_gen_api.open_code_gen_model.model_service import SalesforceCodeGen350M


def cli(prompt: str):
    logger.info("CLI called with prompt: %s", prompt)
    model = SalesforceCodeGen350M()
    result = model.infer(prompt)
    logger.info("Result: %s", result)
    return result


if __name__ == "__main__":
    import sys
    from open_code_gen_api import cli

    if len(sys.argv) < 2:
        sys.exit(f"Usage: {sys.argv[0]} <prompt>")

    result = cli.cli(" ".join(sys.argv[1:]))
    print(result)
