import json
from datetime import datetime
from django.db import connections
from django.core import serializers, management
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from ffxi.models import DailyTally, EnhancedSignetLevels

@csrf_exempt
def get_daily_stats(request):
    if request.POST and request.is_ajax():
        dt = None
        data = None
        try:
            dt = DailyTally.objects.get(user=request.user,
                                                date=request.POST['date'])
        except DailyTally.DoesNotExist:
            dt = DailyTally.objects.create(
                user=request.user,
                date=datetime.strptime(request.POST['date'], "%Y-%m-%d")
            )
        
        estimated_exp = sum([
            dt.jumpjacks * 3,
            dt.high_knees * 3,
            dt.knee_pull_ins * 3,
            dt.cross_crunches * 3,
            dt.pushups * 3,
            dt.squats * 3,
            dt.climbers * 5,
            dt.plank_jumps * 5
        ]) 
        
        data = [{
            'pk': dt.pk,
            'estimated_exp': estimated_exp,
            'fields': {
                'jumpjacks': dt.jumpjacks,
                'high_knees': dt.high_knees,
                'knee_pull_ins': dt.knee_pull_ins,
                'cross_crunches': dt.cross_crunches,
                'pushups': dt.pushups,
                'squats': dt.squats,
                'climbers': dt.climbers,
                'plank_jumps': dt.plank_jumps
            }
        }]

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
        dt = DailyTally.objects.get(user=request.user,
                                            date=request.POST['date'])
        dt.chain = True;
        saved = dt.save();
  
        data = serializers.serialize('json', [dt])
        return HttpResponse(json.dumps(data), "application/json")
    return HttpResponseRedirect('/daily-tasks/')
    
@csrf_exempt
def get_signet_cost(request):
    if request.POST and request.is_ajax():
        cursor = connections['default'].cursor()
        q = """SELECT sum(exp) FROM ffxi_enhancedsignetlevels
               WHERE id > {0} AND id <= {1} LIMIT 1""".format(
               request.POST['start_level'],
               request.POST['final_level']
        )
        cursor.execute(q)
        cost = cursor.fetchone()[0] 
        return HttpResponse(json.dumps({'cost':str(cost)}), "application/json")
    return HttpResponseRedirect('/')
    
@csrf_exempt
def get_level_cost(request):
    if request.POST and request.is_ajax():
        cursor = connections['darkstar'].cursor()
        q = """SELECT sum(`exp`) FROM `exp_base` 
               WHERE `level` > {0} AND `level` <= {1} LIMIT 1""".format(
               request.POST['start_level'],
               request.POST['final_level']
        )
        cursor.execute(q)
        cost = cursor.fetchone()[0] 
        return HttpResponse(json.dumps({'cost':str(cost)}), "application/json")
    return HttpResponseRedirect('/')

@csrf_exempt    
def get_max_level(request):
    if request.POST and request.is_ajax():
        cursor = connections['darkstar'].cursor()
        q = """SELECT `genkai` FROM `char_jobs` 
               WHERE `charid`={0} LIMIT 1""".format(request.POST['charid'])
        cursor.execute(q)
        genkai = cursor.fetchone()[0] 
        return HttpResponse(json.dumps({'genkai':str(genkai)}), "application/json")
    return HttpResponseRedirect('/')
    