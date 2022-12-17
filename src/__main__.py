import sys
from open_code_gen_api import cli

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} <prompt>")

result = cli.cli(" ".join(sys.argv[1:]))
print(result)
