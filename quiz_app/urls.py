from django.urls import path, include

from .views import TestListView, TestView


urlpatterns = [
	path('', TestListView.as_view(), name='TestList'),
	path('test/<int:pk>', TestView.as_view(), name='TestView') 
]