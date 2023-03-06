import openai
import os


def init_openapi(key: str):
    openai.api_key = key
    return openai


def get_openai():
    if openai.api_key:
        return openai
    return init_openapi()
