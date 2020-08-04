from django.urls import path
from . import views


urlpatterns = [
    path('info/', views.coInfo, name='covid19'),
    # path('info/', views.search, name='results'),

]
