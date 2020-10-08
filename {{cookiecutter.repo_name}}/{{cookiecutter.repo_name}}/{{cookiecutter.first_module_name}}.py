"""
{{cookiecutter.first_module_name}}.py
{{cookiecutter.description}}
"""
from . import __version__
from fastapi import FastAPI

app = FastAPI()


@app.get("/version")
def read_version():
    return {"version": __version__}
