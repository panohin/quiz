from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Test

class TestListView(ListView):
    model = Test
    paginate_by = 1

class TestDetail(DetailView):
	model = Test

    