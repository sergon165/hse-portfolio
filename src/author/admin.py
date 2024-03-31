"""
Функции панели управления для приложения "Автор".
"""
from typing import Type, Any

from django.contrib import admin
from django.db.utils import ProgrammingError
from django.http import HttpRequest

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("email",)

    def __init__(self, model: Type[Author], admin_site: admin.AdminSite) -> None:
        super().__init__(model, admin_site)
        try:
            Author.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request: HttpRequest, obj: Any = None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj: Any = None) -> bool:
        return False
