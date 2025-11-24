# config.py
import os

ENVIRONMENTS = {
    "dev": {"model": "gpt-3.5-turbo", "temperature": 0.9, "verbose": True},
    "prod": {"model": "gpt-4", "temperature": 0.3, "verbose": False},
}

ENV = os.getenv("ENV", "dev")
config = ENVIRONMENTS[ENV]




