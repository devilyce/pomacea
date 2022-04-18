from django.urls import path

from . import views

urlpatterns = [
    path('', views.mgmt, name='mgmt'),
    path('search/', views.search_results, name='search_results'),
    path('inquiry_detail/<int:pk>', views.inquiry_detail, name='inquiry_detail'),

    # path('inquiry_detail/<int:pk>', InquiryDetail.as_view(), name='inquiry_detail'),

]
