from django.urls import path
from .views import UsersV
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UsersV.register, name='register'),
    path('register2/', UsersV.register2, name='register2'),
    path('profile/', UsersV.profile, name='profile'),
    path('newjob/', UsersV.newJob, name='newjob'),
    path('jobs/', UsersV.jobs, name='jobs'),
    path('jobs/details/<int:pk>/', UsersV.job_details, name='job_details'),
    path('administrator/', UsersV.administrator, name='administrator'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    ]
