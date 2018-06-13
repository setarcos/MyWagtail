from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

class ArticleIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    parent_page_types = ['home.HomePage', 'ArticlePage']
    subpage_types = ['ArticlePage', 'PuretxtPage']

    class Meta:
        verbose_name = "文章列表"

class ArticlePage(Page):
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    parent_page_types = ['ArticleIndexPage', 'ArticlePage']
    subpage_types = ['ArticlePage', 'PuretxtPage']

    class Meta:
        verbose_name = "一般文章"

class PuretxtPage(Page):
    body = models.TextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    parent_page_types = ['ArticleIndexPage', 'ArticlePage']
    subpage_types = ['ArticlePage', 'PuretxtPage']

    class Meta:
        verbose_name = "纯文本文章"
