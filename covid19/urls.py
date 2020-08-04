from django.urls import path
from . import views


urlpatterns = [
    path('Covid19/', views.coInfo, name='covid19'),
    # path('info/', views.search, name='results'),

]
