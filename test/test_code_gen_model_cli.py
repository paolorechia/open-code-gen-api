from open_code_gen_api import cli

# Test that the model runs
def test_cli(caplog):
    assert "hello world" in cli.cli("hello world")
