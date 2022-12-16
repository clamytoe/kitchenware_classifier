FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "api.py", "kw_router.py", "fastai_model.pkl", "favicon.ico", "./"]

RUN pipenv install --system --deploy

EXPOSE 8000

CMD python -m uvicorn api:app --host 0.0.0.0 --port 8000
