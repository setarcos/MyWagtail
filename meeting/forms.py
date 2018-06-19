from django import forms
import datetime
from .models import RoomAgenda, MeetingRoom

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
        label="日期(固定日期的时间或者每周重复的截止时间)",
        initial=datetime.date.today,
        widget=forms.SelectDateWidget,
    )

    week = forms.ChoiceField(
        required=False,
        label="星期",
        choices=((1, "周一"), (2, "周二"), (3, "周三"), (4, "周四"),
            (5, "周五"), (6, "周六"), (7, "周日")),
    )

    start = forms.TimeField(
        required=True,
        label="起始时间",
    )

    end = forms.TimeField(
        required=True,
        label="结束时间",
    )

    note = forms.CharField(
        required=True,
        label="事由",
        initial="",
    )

    def clean(self):
        super().clean()
        if (not self.is_valid()):
            return
        s = self.cleaned_data.get('start')
        e = self.cleaned_data.get('end')
        if (s >= e):
            raise forms.ValidationError("起始时间要早于结束时间")
        d = self.cleaned_data.get('date')
        if (d < datetime.date.today()):
            raise forms.ValidationError("日期不能在过去")
