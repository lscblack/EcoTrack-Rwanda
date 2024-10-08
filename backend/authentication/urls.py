from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('api/register', views.register, name="register"),
    path('api/schedule', views.schedule, name="schedule"),
    path('api/jobs/available-jobs', views.available_jobs, name="available-jobs"),
    path('api/schedules/my-schedules', views.my_schedules, name="my_schedules"),
    path('api/jobs/manage-job', views.manage_job, name="manage_job"),
    path('api/jobs/my-jobs', views.my_jobs, name="my_jobs"),
    path('api/jobs/<int:id>', views.get_job, name="get_job"),
    path('api/all-users', views.all_users, name="all_users"),
    path('api/logout', views.logout, name="logout"),
    path('api/schedules/all-schedules', views.all_schedules, name="all_schedules"),
    path('api/users/<int:id>', views.get_user, name="get_user"),
    path('api/user/<int:id>/', views.user_detail, name='user_detail'),
    path('api/achievement-data', views.achievement_data, name="achievement_data"),
    path('api/schedules/completed', views.completed_user_schedules, name="completed_user_schedules"),
    path('api/jobs/completed', views.completed_jobs, name="completed_jobs"),
    path('api/count-stats/', views.count_stats, name='count-stats'),
    path('api/github-webhook', views.github_webhook, name="github_webhook"),
]