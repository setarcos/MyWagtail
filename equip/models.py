from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
import time

class EquipIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['EquipPage']

    class Meta:
        verbose_name = "设备目录"

class EquipPage(Page):
    model = models.CharField(max_length=40, verbose_name="型号")
    spec = models.CharField(max_length=100, verbose_name="主要指标")
    madeby = models.CharField(max_length=40, verbose_name="厂家")
    info = models.CharField(max_length=10, verbose_name="简要说明")
    count = models.IntegerField(default=0, verbose_name="数量")
    picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    manual = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('info'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('model'),
        FieldPanel('spec'),
        FieldPanel('madeby'),
        FieldPanel('info'),
        FieldPanel('count'),
        ImageChooserPanel('picture'),
        DocumentChooserPanel('manual'),
    ]

    parent_page_types = ['EquipIndexPage']
    subpage_types = []

    def clean(self):
        super().clean()
        ts_slug = time.time() - 1514736000 # datetime(2018,1,1,0,0,0)
        self.slug = '%d' % ts_slug

    class Meta:
        verbose_name = "设备"
