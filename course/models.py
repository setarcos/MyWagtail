from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, TabbedInterface, ObjectList
from modelcluster.fields import ParentalKey
from wagtail.documents.edit_handlers import DocumentChooserPanel
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

    course_panels = [
        InlinePanel('handouts', label="讲义资料"),
        InlinePanel('group', label="时段信息"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading="基本信息"),
        ObjectList(course_panels, heading="讲义与时段信息"),
        ObjectList(Page.settings_panels, heading="设置", classname="settings"),
    ])

    parent_page_types = ['CourseIndexPage']
    subpage_types = ['news.NewsIndexPage']

    def clean(self):
        super().clean()
        self.slug = self.number

    class Meta:
        verbose_name = "课程"

class CourseHandout(Orderable):
    page = ParentalKey(CoursePage, on_delete=models.CASCADE, related_name='handouts')
    handout = models.ForeignKey(
        'wagtaildocs.Document', on_delete=models.CASCADE, related_name='+',
        verbose_name="讲义资料",
    )

    panels = [
        DocumentChooserPanel('handout'),
    ]

class CourseGroup(Orderable):
    page = ParentalKey(CoursePage, on_delete=models.CASCADE, related_name='group')
    info = models.CharField(max_length=40, verbose_name="时段描述")
    limit = models.IntegerField(default=0, verbose_name="人数上限")

    panels = [
        FieldPanel('info'),
        FieldPanel('limit'),
      #  InlinePanel('member'),
    ]

class GroupMember(models.Model):
    group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE, related_name='member')
    number = models.CharField(max_length=15, verbose_name="学号")
    name = models.CharField(max_length=40, verbose_name="姓名")

    panels = [
        FieldPanel('number'),
        FieldPanel('name'),
    ]
