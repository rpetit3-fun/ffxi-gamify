import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from ffxi.forms import DailyTasksForm
from ffxi.models import DailyTasks

def index(request):
    return render_to_response('index.html', {}, RequestContext(request))
    
def daily_tasks(request):
    if request.user.is_authenticated():
        if request.POST:
            form = DailyTasksForm(request.POST)
            if form.is_valid():
                dailytasks = form.save(request.user, request.POST)
                if request.is_ajax():
                    return HttpResponse('saved')
                else:
                    return HttpResponseRedirect('/daily-tasks/')
            else:
                if request.is_ajax():
                    return HttpResponse(form.errors)
        else:
            form = DailyTasksForm()
            return render_to_response('daily_tasks.html', {'form': form}, RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def missions(request):
    return render_to_response('missions.html', {}, RequestContext(request))


def quests(request):
    return render_to_response('quests.html', {}, RequestContext(request))


def rewards(request):
    return render_to_response('rewards.html', {}, RequestContext(request))

