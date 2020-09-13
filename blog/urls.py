from django.urls import path, include

# import HTML PAGE
from . import views

# Specify indeed project name
app_name = "blog"

urlpatterns = [
    path("", views.all_blogs, name="all_blogs"),
    # refrence HTML e.x. ../blog/1/ or ../blog/2/ e.t.c
    path("<int:blog_id>/", views.detail, name="detail"),
]
