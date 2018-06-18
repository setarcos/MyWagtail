from django.db import models

class MeetingRoom(models.Model):
    room_no = models.CharField(max_length=15, verbose_name="房间号")
    info = models.CharField(max_length=200, blank=True, verbose_name="描述")

    class Meta:
        verbose_name="会议室"
        verbose_name_plural="会议室"

class RoomAgenda(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE, related_name='agenda')
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=40)
    date = models.IntegerField(default=0)
    start_time = models.IntegerField(default=0)
    end_tiem = models.IntegerField(default=0)
