from django.urls import path

from . import views


urlpatterns =[
    path('calc/', views.calc, name='calc'),
    path('notify_calc/', views.notify_calc, name='notify_calc'),
]
