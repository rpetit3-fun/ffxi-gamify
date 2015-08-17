import json
from datetime import datetime

from django.core import serializers, management
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from ffxi.models import DailyTasks, EnhancedSignetLevels

@csrf_exempt
def get_daily_stats(request):
    if request.POST and request.is_ajax():
        dailytasks = None
        data = None
        try:
            dailytasks = DailyTasks.objects.get(user=request.user,
                                                date=request.POST['date'])
        except DailyTasks.DoesNotExist:
            dailytasks = DailyTasks.objects.create(
                user=request.user,
                date=datetime.strptime(request.POST['date'], "%Y-%m-%d")
            )
        data = serializers.serialize('json', [dailytasks])
        return HttpResponse(json.dumps(data), "application/json")
    return HttpResponseRedirect('/daily-tasks/')

@csrf_exempt
def update_steps(request):
    if request.is_ajax():
        date = request.POST['date']
        name = 'rpetit'
        management.call_command('update_steps', name, request.user.username, date)

        return HttpResponse(json.dumps({'done': 'done'}), "application/json")
    return HttpResponseRedirect('/daily-tasks/')
    
@csrf_exempt
def add_exp_chain(request):
    if request.POST and request.is_ajax():
        dailytasks = DailyTasks.objects.get(user=request.user,
                                            date=request.POST['date'])
        dailytasks.chain = True;
        saved = dailytasks.save();
  
        data = serializers.serialize('json', [dailytasks])
        return HttpResponse(json.dumps(data), "application/json")
    return HttpResponseRedirect('/daily-tasks/')
    
@csrf_exempt
def get_signet_cost(request):
    if request.POST and request.is_ajax():
        cost = EnhancedSignetLevels.objects.get(id=request.POST['level'])  
        data = serializers.serialize('json', [cost])
        return HttpResponse(json.dumps(data), "application/json")
    return HttpResponseRedirect('/')

    