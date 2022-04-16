from django.urls import path

from . import views

urlpatterns = [
    path('', views.mgmt, name='mgmt'),
    path("search/", views.search_results, name="search_results"),
]
