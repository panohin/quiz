from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Test, Question

class TestListView(ListView):
    model = Test
    

class TestView(ListView):
	model = Question
	template_name= 'quiz_app/questions.html'
	paginate_by = 1

	def get_queryset(self):
		queryset = Test.objects.get(pk=self.kwargs['pk']).questions.all()
		return queryset

    