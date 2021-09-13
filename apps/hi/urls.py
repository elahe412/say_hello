from django.urls import path

from apps.hi.views import say_hello, say_my_name

urlpatterns = [
    path('say_hello/', say_hello),
    path('say_my_name/', say_my_name),
]
