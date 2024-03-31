from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Click, Scroll, TimeSpent
import json
from django.shortcuts import render


def analytics(request):
    # Query the last 100 of each model or adjust the number as needed
    clicks = Click.objects.all().order_by('-created_at')[:100]
    scrolls = Scroll.objects.all().order_by('-created_at')[:100]
    time_spent_records = TimeSpent.objects.all().order_by('-created_at')[:100]

    # Pass the queries to the template context
    context = {
        'clicks': clicks,
        'scrolls': scrolls,
        'time_spent_records': time_spent_records,
    }
    return render(request, 'analytics/analytics.html', context)

@csrf_exempt
def save_click(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Click.objects.create(tag_name=data['tagName'])
        return JsonResponse({"status": "success"})

@csrf_exempt
def save_scroll(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Scroll.objects.create(position=data['position'])
        return JsonResponse({"status": "success"})

@csrf_exempt
def save_time_spent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        TimeSpent.objects.create(time_spent=data['timeSpent'])
        return JsonResponse({"status": "success"})

