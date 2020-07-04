from django.urls import path
from . import views


urlpatterns = [
    path('CoronavirusUpdates/', views.coInfo, name='CovUpdate'),
    # path('info/', views.search, name='results'),

]
