# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from {{ cookiecutter.repo_name }} import __version__, app

client = TestClient(app)