'''

'''
import pytz
import subprocess
from optparse import make_option
from datetime import date, datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from ffxi.models import DailyTasks


class Command(BaseCommand):
    help = 'Insert steps from yesterday into database.'
    option_list = BaseCommand.option_list + (
        make_option('--name', dest='name',
                    help='Name to look up steps for.'),
        make_option('--username', dest='username',
                    help='User ID to store the results under.'),
        make_option('--date', dest='date',
                    help='Date to look up steps for (Default: yesterday).'),
    )


    def handle(self, *args, **options):
        # Required Parameters
        if not options['name']:
            if args[0]:
                options['name'] = args[0]
            else:
                raise CommandError('--name')
        if not options['username']:
            if args[1]:
                options['username'] = args[1]
            else:
                raise CommandError('--username')
        if not options['date']:
            if args[2]:
                options['date'] = args[2]
            else:
                yesterday = datetime.now(pytz.timezone('US/Eastern')) - timedelta(1)
                yesterday = datetime.strftime(yesterday, "%Y-%m-%d")
                options['date'] = yesterday

        cmd = ['python', '/home/rpetit/fitbit-steps/fitbit-steps.py',
               '--name', options['name'], '--date', options['date']]

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        steps, error = p.communicate()

        user = User.objects.get(username=options['username'])
        try:
            dailytasks = DailyTasks.objects.get(user=user,
                                                date=options['date'])
            dailytasks.steps = int(steps)
            dailytasks.save()
        except DailyTasks.DoesNotExist:
            dailytasks = DailyTasks.objects.create(user=user,
                                                   date=options['date'],
                                                   steps=int(steps))
            dailytasks.save()                                       
