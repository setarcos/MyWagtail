from django import forms
import datetime

class AgendaForm(forms.Form):
    repeatable = forms.ChoiceField(
        required=True,
        label="日程类型",
        error_messages={'required': "日程类型必须选择"},
        choices=((1, "固定日期"), (2, "每周重复")),
        widget=forms.RadioSelect,
    )

    date = forms.DateField(
        required=False,
        label="日期",
        initial=datetime.date.today,
        widget=forms.SelectDateWidget,
    )

    week = forms.ChoiceField(
        required=False,
        label="星期",
        choices=((1, "周一"), (2, "周二"), (3, "周三"), (4, "周四"),
            (5, "周五"), (6, "周六"), (7, "周日")),
    )

    note = forms.CharField(
        required=True,
        label="事由",
        initial="",
    )
