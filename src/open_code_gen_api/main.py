"""Main API module"""
from fastapi import FastAPI

from open_code_gen_api import request_types
from open_code_gen_api.open_code_gen_model import model_service

app = FastAPI()
VERSION = "0.1"

ModelClass = model_service.SalesforceCodeGen350M
model = ModelClass()


@app.get("/")
async def root():
    """Root endpoint. Get info about which model is running."""
    return {
        "app": "Open Code Gen API",
        "version": VERSION,
        "model": ModelClass.__name__,
        "help": "Call POST /prompt to request a response from the model",
    }


@app.post("/prompt")
async def prompt_handler(request: request_types.PromptRequest):
    """Prompt handler: runs a prompt through the mdoel"""
    result = model.infer(request.prompt_text, request.max_response_length)
    return {"model_response": result}
