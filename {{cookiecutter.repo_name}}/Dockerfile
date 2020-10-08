
FROM python:3.7-slim-buster

COPY install_packages.sh .
RUN ./install_packages.sh

RUN useradd cheminfo

WORKDIR /home/cheminfo

COPY requirements.txt .

COPY app.py .
COPY {{cookiecutter.repo_name}} ./{{cookiecutter.repo_name}}

COPY README.md .

COPY gunicorn_conf.py .

RUN pip install --no-cache-dir -r requirements.txt

USER cheminfoƒ

CMD gunicorn -t 150 -b 0.0.0.0:$PORT -c gunicorn_conf.py --log-level debug --capture-output --enable-stdio-inheritance app:app
