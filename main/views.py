from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
class MainIndex(View):
    def get(self, request):
        return render(request, 'main/index.html')