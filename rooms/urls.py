from django.urls import path

from rooms.views import RoomDetail, RoomList

urlpatterns = [
    path('rooms', RoomList.as_view()),
    path('rooms/<str:pk>', RoomDetail.as_view())
]
