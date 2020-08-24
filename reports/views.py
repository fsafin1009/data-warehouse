from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Report, Category
from .forms import ReportForm
# Create your views here.


def index(request):
    reports = Report.objects.all()
    context = {
        'reports' : reports,
        'title': 'Список статей'
    }
    return render(request, template_name='reports/index.html', context = context)


def get_category(request, category_id):
    reports = Report.objects.filter(category_id = category_id)
    category =  Category.objects.get(pk = category_id)

    context = {
        'reports': reports,
        'category': category,
    }
    return render(request, template_name='reports/category.html', context=context)


def view_reports(request, report_id):
    report_item = get_object_or_404(Report, pk=report_id)
    return render(request, 'reports/view_report.html', {'report_item': report_item})

def add_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = Report.objects.create(**form.cleaned_data)
            return redirect(report)

    else:
        form =  ReportForm()
    return render(request, 'reports/add_report.html',{'form': form} )
