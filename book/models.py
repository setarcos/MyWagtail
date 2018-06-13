from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
import time

class BookIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['BookPage']

    class Meta:
        verbose_name = "书籍目录"

class BookPage(Page):
    author = models.CharField(max_length=40, verbose_name="作者")
    pubhouse = models.CharField(max_length=40, verbose_name="出版社")
    year = models.CharField(max_length=10, verbose_name="出版年")
    note = models.CharField(blank=True, max_length=100, verbose_name="备注")
    content = RichTextField(blank=True, verbose_name="目录")
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('pubhouse'),
        FieldPanel('year'),
        FieldPanel('note'),
        FieldPanel('content', classname="full"),
        ImageChooserPanel('cover'),
    ]

    parent_page_types = ['BookIndexPage']
    subpage_types = []

    def clean(self):
        super().clean()
        ts_slug = time.time() - 1514736000 # datetime(2018,1,1,0,0,0)
        self.slug = '%d' % ts_slug

    class Meta:
        verbose_name = "书籍"
