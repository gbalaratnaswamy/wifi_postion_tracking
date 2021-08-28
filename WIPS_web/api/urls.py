from django.urls import path

from .views import *

urlpatterns = [
    path("api/<unique_id>/", set_aps),
    path("api/<unique_id>/view", view_aps),
    path("apps/<unique_id>/view", view_aps_gui),

]
