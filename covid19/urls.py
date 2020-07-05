from django.urls import path
from . import views


urlpatterns = [
    path('Covid19Info/', views.coInfo, name='CovUpdate'),
    # path('info/', views.search, name='results'),

]
