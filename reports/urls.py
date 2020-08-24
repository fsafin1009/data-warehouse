from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name = "category"),
    path('reports/<int:report_id>/', view_reports, name = "view_reports"),
    path('reports/add-report/', add_report, name = "add_report"),
]