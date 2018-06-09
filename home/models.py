from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from news.models import NewsPage

class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('gallery_images', label="首页图片"),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['newspage'] = NewsPage.objects.live().order_by("-date")[:10]
        return context

    class Meta:
        verbose_name = "首页"

class HomePageGallery(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    url = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        FieldPanel('url'),
    ]
