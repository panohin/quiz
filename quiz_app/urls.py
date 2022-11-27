from django.urls import path, include

from .views import TestListView, TestDetail


urlpatterns = [
	path('', TestListView.as_view(), name='TestList'),
	path('test/<int:pk>', TestDetail.as_view(), name='TestDetail') 
]