from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    pass

    class Meta:
        verbose_name = "首页"
