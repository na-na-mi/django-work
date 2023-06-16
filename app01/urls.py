from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rfm", views.rfm, name="rfm"),
    path("four", views.four, name="four"),
    path("one", views.one, name="one"),
    path("third", views.third, name="third"),
    path("five", views.five, name="five"),
    path("two", views.two, name="two"),
    path("second", views.second, name="second"),
    path("three", views.three, name="three"),
    # path("six", views.six, name="six"),
    path("ra", views.ra, name="ra")
]