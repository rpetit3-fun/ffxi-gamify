import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from ffxi.forms import DailyTallyForm, LinkAccountForm, CharacterUpgradeForm, EnhancedSignetUpgrade
from ffxi.models import DailyTally, LinkedAccount

def index(request):
    return render_to_response('index.html', {}, RequestContext(request))
    
def daily_tally(request):
    if request.user.is_authenticated():
        if request.POST:
            form = DailyTallyForm(request.POST)
            if form.is_valid():
                dt = form.save(request.user, request.POST)
                if request.is_ajax():
                    return HttpResponse('saved')
                else:
                    return HttpResponseRedirect('/daily-tally/')
            else:
                if request.is_ajax():
                    return HttpResponse(form.errors)
        else:
            form = DailyTallyForm()
            return render_to_response('daily_tally.html', {'form': form}, RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def link_account(request):
    if request.user.is_authenticated():
        if request.POST:
            form = LinkAccountForm(request.POST)
            if form.is_valid():
                status = form.save(request.user, request.POST)
                if status[0]:
                    # Has Character, send to that page!
                    url = '/character/{0}/{1}/'.format(
                        status[1]['charid'],
                        status[1]['charname']
                    )
                    return HttpResponseRedirect(url)
                else:
                    return render_to_response(
                        'link_account.html',
                        {'form': form},
                        RequestContext(request)
                    )
            else:
                return render_to_response(
                    'link_account.html', {'form': form}, RequestContext(request)
                )
        else:
            form = LinkAccountForm()
            return render_to_response('link_account.html', {'form': form}, RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def character(request, charid, charname):
    if request.user.is_authenticated():
        if request.POST:
            form = None
            if request.POST['form'] == 'character':
                form = CharacterUpgradeForm(request.POST, charid=charid)
            else:
                form = EnhancedSignetUpgrade(request.POST, charid=charid)
                
            if form.is_valid(request.user):
                saved = form.save(request.user)
                if request.is_ajax():
                    return HttpResponse(saved)
                else:
                    return HttpResponseRedirect('/character/'+charid+"/"+charname+"/")
            else:
                if request.is_ajax():
                    return HttpResponse(request.POST['char_cost'])
                else:
                    return HttpResponseRedirect('/character/'+charid+"/"+charname+"/")
        else:
            form_character = CharacterUpgradeForm(charid=charid)
            form_signet = EnhancedSignetUpgrade(charid=charid)
            return render_to_response('character.html', 
                {'charid':charid, 'charname':charname, 
                'form_character':form_character, 'form_signet':form_signet},
                RequestContext(request)
        )
    else:
        return HttpResponseRedirect('/')

        
def missions(request):
    return render_to_response('missions.html', {}, RequestContext(request))


def quests(request):
    return render_to_response('quests.html', {}, RequestContext(request))


def rewards(request):
    return render_to_response('rewards.html', {}, RequestContext(request))

