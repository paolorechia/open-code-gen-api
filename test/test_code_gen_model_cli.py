from open_code_gen_api.open_code_gen_model import cli

def test_cli():
    assert cli.hello_cli() == "hello-cli"
