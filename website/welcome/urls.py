from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from . import views
urlpatterns = [
    path("<username>/<festival>", views.display),

]
#buddadibba2002