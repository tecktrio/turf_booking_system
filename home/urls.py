from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('profile',views.profile),
    path('contact/',views.contact),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('delete/<str:turf_name>',views.delete),
    path('book/<str:id>',views.book),
    path('bookturf',views.bookturf),
    path('manage',views.manage),
    path('add_turf',views.add_turf),
    path('edit_turf/<int:id>',views.edit_turf),
]