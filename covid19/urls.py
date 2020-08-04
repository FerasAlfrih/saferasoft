from django.urls import path
from . import views


urlpatterns = [
    path('', views.coInfo, name='covid19'),
    # path('info/', views.search, name='results'),

]
