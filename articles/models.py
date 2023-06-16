from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    author = models.CharField(max_length=256, verbose_name=_("author"), null=True, blank=True)
    title = models.CharField(max_length=256, verbose_name=_("title"), null=True, blank=True)
    description = models.TextField(verbose_name=_("description"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"
