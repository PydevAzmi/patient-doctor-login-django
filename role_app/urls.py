from django.urls import path
from .views import login
app_name = 'role_app'
urlpatterns = [
    path('' , login , name= 'home_page'),

]