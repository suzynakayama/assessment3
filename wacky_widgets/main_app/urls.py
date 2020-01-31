from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_widget, name="add_widget"),
    path('<int:pk>/delete/', views.WidgetDelete.as_view(), name="delete_widget"),
]