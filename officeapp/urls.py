from officeapp.api_views import (OfficeListView, OfficeCreateUpdateDeleteView,
                                 RoomListView, RoomCreateUpdateDeleteView,
                                 SeatListView, SeatDetailView)
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'offices', OfficeListView)
router.register(r'office', OfficeCreateUpdateDeleteView)
router.register(r'rooms', RoomListView)
router.register(r'room', RoomCreateUpdateDeleteView)
router.register(r'seats', SeatListView)
router.register(r'seat', SeatDetailView)
urlpatterns = router.urls