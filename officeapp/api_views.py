from officeapp.serializers import (AddressSerializer,
                                   RoomSerializer,
                                   SeatSerializer,
                                   SeatDetailSerializer,
                                   UserSerializer,
                                   RegisterSerializer)
from officeapp.models import Office, Room, Seat
from rest_framework import viewsets, generics, mixins, permissions
from django_filters import rest_framework as filters
from django.contrib.auth import login
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class OfficeListView(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Office.objects.all()
    serializer_class = AddressSerializer

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('address', )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class OfficeCreateUpdateDeleteView(viewsets.mixins.CreateModelMixin,
                       viewsets.mixins.RetrieveModelMixin,
                       viewsets.mixins.UpdateModelMixin,
                       viewsets.mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):

    queryset = Office.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'id'
    permission_classes = (permissions.IsAdminUser, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class RoomListView(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('room_number', )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RoomCreateUpdateDeleteView(viewsets.mixins.CreateModelMixin,
                       viewsets.mixins.RetrieveModelMixin,
                       viewsets.mixins.UpdateModelMixin,
                       viewsets.mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'
    permission_classes = (permissions.IsAdminUser, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SeatListView(viewsets.mixins.ListModelMixin,
                   viewsets.mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('seat_number', 'is_free', 'start')


class SeatDetailView(viewsets.mixins.RetrieveModelMixin,
                     viewsets.mixins.DestroyModelMixin,
                     viewsets.mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatDetailSerializer

    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)