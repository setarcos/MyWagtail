from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

class CourseIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['CoursePage']

    class Meta:
        verbose_name = "课程列表"

class CoursePage(Page):
    name = models.CharField(max_length=20, verbose_name="课程名")
    ename = models.CharField(max_length=100, verbose_name="英文名称")
    number = models.CharField(max_length=10, verbose_name="课程编号")
    teacher = models.CharField(max_length=20, verbose_name="授课教师")
    teaid = models.CharField(max_length=12, verbose_name="教师工资号")
    unit = models.IntegerField(default=0, verbose_name="学分")
    hours = models.IntegerField(default=0, verbose_name="课时")
    terms = models.CharField(max_length=20, verbose_name="授课学期")
    body = RichTextField(blank=True, verbose_name="课程大纲")

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('ename'),
        FieldPanel('number'),
        FieldPanel('teacher'),
        FieldPanel('teaid'),
        FieldPanel('unit'),
        FieldPanel('hours'),
        FieldPanel('terms'),
        FieldPanel('body', classname="full"),
    ]

    promote_panels = []

    parent_page_types = ['CourseIndexPage']
    subpage_types = ['news.NewsPage']

    def clean(self):
        super().clean()
        self.slug = self.number

    class Meta:
        verbose_name = "课程"
