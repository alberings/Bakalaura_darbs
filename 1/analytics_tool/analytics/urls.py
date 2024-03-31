# analytics/urls.py

from django.urls import path
from . import views
from .views import save_click, save_scroll, save_time_spent

urlpatterns = [
   path('save_click/', save_click, name='save_click'),
    path('save_scroll/', save_scroll, name='save_scroll'),
    path('save_time_spent/', save_time_spent, name='save_time_spent'),
    path('analytics/', views.analytics, name='analytics'),
]
