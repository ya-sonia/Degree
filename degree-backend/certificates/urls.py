from django.urls import path

from .views import certificate_view


urlpatterns = [

    path(
        'certificate/<str:registration_no>/',
        certificate_view,
        name='certificate'
    ),
]