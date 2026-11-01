from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('del_etud/<int:id>', views.del_etud, name='del_etud')
]