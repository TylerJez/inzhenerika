"""
URL configuration for inzhenerika project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import calc.views
import review.views
from review import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('calc.html', calc.views.calc, name='calc'),
    path('feedback/', include('review.urls')),
    path('feedback.html', views.ReviewView.as_view()),
    path('feedback-form.html', review.views.review),
    path('notify_review/', review.views.notify_review),
    path('notify_calc/', calc.views.notify_calc, name='notify_calc')
]