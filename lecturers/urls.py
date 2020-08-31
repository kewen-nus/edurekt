from django.urls import path

from lecturers.views import LecturerDetail, LecturerList

urlpatterns = [
    path('lecturers', LecturerList.as_view()),
    path('lecturers/<int:pk>', LecturerDetail.as_view())
]
