from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Report
from .serializers import ReportSerializer
from django.views.generic import TemplateView

def report_list(request):
    reports = Report.objects.all()
    serializer = ReportSerializer(reports, many=True)
    return JsonResponse(serializer.data, safe=False)

def report_detail(request, pk):
    try:
        report = Report.objects.get(pk=pk)
    except Report.DoesNotExist:
        return JsonResponse({'error': 'Report not found'}, status=404)

    serializer = ReportSerializer(report)
    return JsonResponse(serializer.data)

def generate_report(request):
    # Logic for generating a report can be added here
    return render(request, 'reports/report.html')

class ReportListView(View):
    """
    Class-based view returning a JSON list of reports.
    URL: apps/reports/urls.py -> ReportListView.as_view()
    """
    def get(self, request, *args, **kwargs):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return JsonResponse(serializer.data, safe=False)

class ReportDetailView(View):
    """
    Class-based view returning JSON for a single report.
    URL: apps/reports/urls.py -> ReportDetailView.as_view()
    """
    def get(self, request, pk, *args, **kwargs):
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(report)
        return JsonResponse(serializer.data)

class ReportFrontendView(TemplateView):
    """
    Frontend for reports - shows list and simple visualization of report.data
    """
    template_name = "reports/reports.html"