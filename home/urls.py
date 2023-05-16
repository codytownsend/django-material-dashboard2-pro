from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Pages -> Jobs
    path('jobs/', views.discover, name="jobs"),
    path('jobs/new-user/', views.new_job, name="new_job"),

]
