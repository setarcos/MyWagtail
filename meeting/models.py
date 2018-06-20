from django.db import models

class MeetingRoom(models.Model):
    room_no = models.CharField(max_length=15, verbose_name="房间号")
    info = models.CharField(max_length=200, blank=True, verbose_name="描述")

    class Meta:
        verbose_name="会议室"
        verbose_name_plural="会议室"

    def get_agenda(self):
        return self.agenda.all()

    # to check if the agenda is without conflict
    def isOK(self, day, start, end):
        return True


class RoomAgenda(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE, related_name='agenda')
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=40)
    date = models.IntegerField(default=0)
    start_time = models.TimeField(default='00:00')
    end_time = models.TimeField(default='00:00')

    def strdate(self):
        return '{0}年{1}月{2}日'.format(int(self.date / 10000), int(self.date % 10000 / 100), self.date % 100)