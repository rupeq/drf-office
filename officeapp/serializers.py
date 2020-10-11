from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from officeapp.models import *

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('id', 'address')

# class RoomCreateSerializer(serializers.Serializer):
#     room_number = serializers.CharField(required=True)
#     office = serializers.SlugRelatedField(many=False,
#                                           slug_field="address",
#                                           queryset=Office.objects.all())
#     def create(self, validated_data):
#         return Room.objects.create(**validated_data)


class RoomSerializer(serializers.ModelSerializer):
    office = serializers.SlugRelatedField(many=False,
                                          slug_field="address",
                                          queryset=Office.objects.all())
    class Meta:
        model = Room
        fields = ('id', 'room_number', 'office')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class SeatSerializer(serializers.Serializer):
    seat_number = serializers.CharField(required=True)
    room = serializers.SlugRelatedField(many=False,
                                        slug_field="room_number",
                                        queryset=Room.objects.all())
    is_free = serializers.BooleanField(read_only=True, default=False)
    owner = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        now = timezone.now()
        start = validated_data['start']
        end = validated_data['end']
        if start < now < end:
            validated_data['is_free'] = False
        elif end < now or start > now or (end > now and start > now) or (end < now and start < now):
            validated_data['is_free'] = True
        if 'owner' not in validated_data:
             validated_data['owner'] = self.context['request'].user
        return Seat.objects.create(**validated_data)

class SeatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('id', 'owner', 'seat_number', 'is_free', 'start', 'end')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        return user

