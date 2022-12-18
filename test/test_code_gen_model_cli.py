# pylint: disable=missing-module-docstring, import-error, missing-function-docstring

from open_code_gen_api import cli  # type: ignore


# Test that the model runs
def test_cli():
    assert "hello world" in cli.cli("hello world")
