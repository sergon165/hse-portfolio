from typing import Any

from django.db import models


# Create your models here.
class SingletonModel(models.Model):
    """
    Абстрактная модель для реализации паттерна Singleton.
    """

    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.__class__.objects.exclude(id=self.pk).delete()
        super().save(*args, **kwargs)

    @classmethod
    def load(cls) -> "SingletonModel":
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class Author(SingletonModel):
    """
    Модель автора сайта.
    """

    cv_link = models.URLField(verbose_name="Ссылка на резюме")
    github_link = models.URLField(verbose_name="Ссылка на GitHub")
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "Автор сайта"
        verbose_name_plural = "Авторы сайта"

    def __str__(self) -> str:
        return f'Объект "Автор сайта" (id={self.pk})'
