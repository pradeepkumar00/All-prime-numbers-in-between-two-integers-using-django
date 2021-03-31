from django.urls import path #we have import only path because admin urls define in main project #primeno
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('calculate',views.calculate, name="prime no"),
]