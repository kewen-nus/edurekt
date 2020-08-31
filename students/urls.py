from django.urls import path

from students.views import StudentDetail, StudentList

urlpatterns = [
    path('students', StudentList.as_view()),
    path('students/<str:pk>', StudentDetail.as_view())
]
