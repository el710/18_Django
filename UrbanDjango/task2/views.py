from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def indexf(request):
    return render(request, "indexf.html")

class IndexC(TemplateView):
    template_name = "indexc.html"
