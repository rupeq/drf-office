from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Office(models.Model):
    address = models.CharField('Address', max_length=200)

    def __repr__(self):
        add = self.address or '[No Address]'
        return f'<Office object "{add}">'

    def __str__(self):
        return self.address


class Room(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='office_room', null=True, blank=True)
    room_number = models.CharField("Room number", max_length=30)

    def __repr__(self):
        return f'<Room object ({self.room_number})>'

    def __str__(self):
        return f'Room {self.room_number}, office {self.office.address}'


class Seat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    seat_number = models.CharField("seat_number", max_length=30)
    is_free = models.BooleanField(default=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __repr__(self):
        return f'<Seat object "{self.seat_number}">'

    def __str__(self):
        return f'Seat {self.seat_number}, room {self.room.room_number}'
