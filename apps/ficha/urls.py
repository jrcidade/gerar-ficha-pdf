from django.urls import path, re_path
from apps.ficha import views

urlpatterns = [

    # The home page
    path('', views.index, name='ficha'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='ficha'),

]

