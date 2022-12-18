FROM python:3.10.9-bullseye

COPY models /models
COPY requirements.txt /
RUN ["pip", "install", "-r", "/requirements.txt"]
COPY src /src
WORKDIR /src
ENV OPEN_CODE_GEN_API_MODEL_PATH=/models

ENTRYPOINT [ "uvicorn", "open_code_gen_api.main:app", "--host", "0.0.0.0"]
