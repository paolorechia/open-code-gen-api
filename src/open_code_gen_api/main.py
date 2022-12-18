from fastapi import FastAPI
from open_code_gen_api.open_code_gen_model import model_service
from open_code_gen_api import request_types

app = FastAPI()
version = "0.1"

model_class = model_service.SalesforceCodeGen350M
model = model_class()


@app.get("/")
async def root():
    return {
        "app": "Open Code Gen API",
        "version": version,
        "model": model_class.__name__,
        "help": "Call POST /prompt to request a response from the model",
    }


@app.post("/prompt")
async def prompt_handler(request: request_types.PromptRequest):
    result = model.infer(request.prompt_text)
    return {"model_response": result}
