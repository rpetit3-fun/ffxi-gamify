'''

'''
import pytz
import sys
import subprocess
from optparse import make_option
from datetime import date, datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from ffxi.models import DailyTasks, ExperienceStats, ExperienceHistory

class Command(BaseCommand):
    help = 'Calculate experience points for yesterday.'

    def handle(self, *args, **options):
        # Required Parameters
        yesterday = datetime.now(pytz.timezone('US/Eastern')) - timedelta(1)
        yesterday = datetime.strftime(yesterday, "%Y-%m-%d")

        for user in User.objects.all():
            self.update_steps(user, yesterday)
            self.daily_task_exp(user, yesterday)
                
    def update_steps(self, user, date):
        cmd = ['python', '/home/rpetit/fitbit-steps/fitbit-steps.py',
               '--name', user.username, '--date', date]

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        steps, error = p.communicate()

        try:
            dailytasks = DailyTasks.objects.get(user=user,
                                                date=date)
            dailytasks.steps = int(steps)
            dailytasks.save()
        except DailyTasks.DoesNotExist:
            dailytasks = DailyTasks.objects.create(user=user,
                                                   date=date,
                                                   steps=int(steps))
            dailytasks.save()
    
    def daily_task_exp(self, user, date):
        dt = DailyTasks.objects.get(user=user, date=date)
        current_exp_chain = None
        total_exp = 0.0
        if dt.chain:
            try:
                exp_stats = ExperienceStats.objects.get(user=user)
                # Experience modifier can't exceed 5x (100 days w/o missing a workout)
                current_exp_chain = min([5.0, float(exp_stats.chain) + 0.05])
            except ExperienceStats.DoesNotExist:
                exp_stats = ExperienceStats.objects.create(user=user, exp=0, chain=1)
                exp_stats.save()
                current_exp_chain = 1
        else:
            current_exp_chain = 1.0
            
        # Sum up the points, need to move difficulty to db
        total_exp += dt.steps
        total_exp += dt.jumpjacks * 3.0
        total_exp += dt.high_knees * 3.0
        total_exp += dt.plank_jumps * 5.0
        total_exp += dt.pushups * 3.0
        total_exp += dt.squats * 3.0
        total_exp += dt.climbers * 5.0
        total_exp += dt.knee_pull_ins * 3.0
        total_exp += dt.cross_crunches * 3.0
        total_exp = int(total_exp * current_exp_chain)
        
        # Add xp to tables
        exp_stats, created = ExperienceStats.objects.get_or_create(user=user)
        exp_stats.exp += total_exp
        exp_stats.chain = current_exp_chain
        exp_stats.save()
        
        exp_history = ExperienceHistory.objects.create(
            user=user,
            date=date,
            exp=total_exp,
            chain=current_exp_chain
        )
        
        print "{0}\t{1}\t{2}".format(user.username, total_exp, current_exp_chain)