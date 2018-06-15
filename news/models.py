from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.documents.models import Document
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.search import index
import time

class NewsIndexPage(Page):
    def get_context(self, request):
        context = super(NewsIndexPage, self).get_context(request)

        allnews = NewsPage.objects.child_of(self);
        # I cant' use self.get_children().live().order_by because date is not a page field.
        allpages = allnews.live().order_by('-date')
        paginator = Paginator(allpages, 10) # Show 10 resources per page
        page = request.GET.get('page')
        try:
            newspages = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            newspages = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            newspages = paginator.page(paginator.num_pages)
        context['newspages'] = newspages
        return context

    parent_page_types = ['home.HomePage', 'course.CoursePage']
    subpage_types = ['NewsPage']

    class Meta:
        verbose_name = "新闻通知列表"

class NewsPage(Page):
    date = models.DateField(verbose_name="发布日期")
    body = RichTextField(blank=True, verbose_name="正文")

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        InlinePanel('news_attach', label="新闻附件"),
    ]

    promote_panels = []

    parent_page_types = ['NewsIndexPage']
    subpage_types = [] # no subpage allowed

    def clean(self):
        super().clean()
        ts_slug = time.time() - 1514736000 # datetime(2018,1,1,0,0,0)
        # I don't care meaningful slug names here, so just use a timestamp
        self.slug = '%d' % ts_slug

    class Meta:
        verbose_name = "新闻通知"

class NewsPageAttach(Orderable):
    page = ParentalKey(NewsPage, on_delete=models.CASCADE, related_name='news_attach')
    attach = models.ForeignKey(
        'wagtaildocs.Document', on_delete=models.CASCADE, related_name='+',
        verbose_name="附件",
    )

    panels = [
        DocumentChooserPanel('attach'),
    ]
