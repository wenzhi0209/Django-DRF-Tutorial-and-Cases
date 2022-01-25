from django.urls import path
from .views import Index,Polls,Poll_details

urlpatterns = [
    path('',Index,name='index'),
    path('polls/',Polls,name='polls_list'),
    path('polls/<int:poll_id>',Poll_details,name='poll_details'),
]
