from django.urls import path, include
from . import views

app_name = "blogg"

urlpatterns = [

    path('', views.all_bloggs, name = 'all_bloggs'),
    path('<int:blogg_id>/', views.detail, name = 'detail'),


]
