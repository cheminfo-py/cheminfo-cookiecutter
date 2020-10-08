
FROM python:3.7-slim-buster

COPY install_packages.sh .
RUN ./install_packages.sh

RUN useradd cheminfo

WORKDIR /home/cheminfo

COPY requirements.txt .

COPY app.py .
COPY {{cookiecutter.repo_name}} ./{{cookiecutter.repo_name}}

COPY README.md .

RUN pip install --no-cache-dir -r requirements.txt

USER cheminfo

CMD gunicorn -w 4 {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}}:app --host 0.0.0.0 --port $PORT -k uvicorn.workers.UvicornWorker
