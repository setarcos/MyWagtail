from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
import time

class NewsIndexPage(Page):
    class Meta:
        verbose_name = "新闻通知列表"

class NewsPage(Page):
    date = models.DateField("Post date")
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]

    def clean(self):
        super().clean()
        ts_slug = time.time() - 1514736000 # datetime(2018,1,1,0,0,0)
        # I don't care meaningful slug names here, so just use a timestamp
        self.slug = '%d' % ts_slug

    class Meta:
        verbose_name = "新闻通知"
