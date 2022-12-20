from django.urls import path
from clinic import views

urlpatterns = [
    path('clinic/', views.ClinicView.as_view(), name='clinic_top'),
]