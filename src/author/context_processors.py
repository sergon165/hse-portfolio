from django.http import HttpRequest

from author.models import Author


def load_author(request: HttpRequest) -> dict:
    return {"author": Author.load()}
