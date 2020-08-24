from django.shortcuts import render
from django.http import HttpResponse
from .models import Report, Category

# Create your views here.


def index(request):
    reports = Report.objects.all()
    context = {
        'reports' : reports,
        'title': 'Список статей'
    }
    return render(request, template_name='reports/index.html', context = context)


