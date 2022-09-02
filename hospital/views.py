from django.shortcuts import render, get_object_or_404
from .models import *
def index(request):
    return render(request, 'index.html')

def docDetail(request, pk):
    doc = get_object_or_404(Doctor, pk=pk)
    context = {
        'doctor' : doc
    }
    return render(request, 'docdetail.html', context=context)