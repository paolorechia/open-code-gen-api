# pylint: disable=missing-module-docstring, import-error, missing-function-docstring

from fastapi.testclient import TestClient

from open_code_gen_api.main import app  # type: ignore

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "app": "Open Code Gen API",
        "help": "Call POST /prompt to request a response from the model",
        "model": "SalesforceCodeGen350M",
        "version": "0.1",
    }


def test_prompt():
    response = client.post("/prompt", json={"prompt_text": "test"})
    assert response.status_code == 200
    response = response.json()
    assert response["model_response"]
