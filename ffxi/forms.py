from collections import OrderedDict
from django.db import connections

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.db.utils import IntegrityError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from registration.forms import RegistrationFormUniqueEmail

from ffxi.form_constants import *
from ffxi.models import DailyTasks, LinkedAccount
from darkstar.models import Accounts

class RegistrationFormWithName(RegistrationFormUniqueEmail):
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

class DailyTasksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DailyTasksForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Save'))
        css = 'col-sm-6'
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_id = 'save-daily-task'
        self.helper.form_class = 'input-lg'
        self.helper.form_action = ''
        
        fields = ['jumpjacks', 'high_knees', 'plank_jumps', 
                  'pushups', 'squats', 'climbers', 'knee_pull_ins', 
                  'cross_crunches', 'date']
        
        self.helper.layout = Layout(
            Div(
                'jumpjacks', 'high_knees', 'plank_jumps', 'pushups',
                css_class=css
            ),
            Div(
                'climbers', 'knee_pull_ins', 'cross_crunches', 'squats',
                css_class=css
            ),
            Div(
                
                Div(Submit('submit', 'Save', css_class='btn-lg'), css_class='col-sm-4'),
                css_class='row col-md-12 col-md-offset-10 submit_buttons'
            ),
            Field('date', type='hidden'),
        )

    def save(self, user, POST):
        try:
            # Exists so lets update
            dailytasks = DailyTasks.objects.get(user=user, date=POST['date'])
            dailytasks.jumpjacks = POST['jumpjacks']
            dailytasks.high_knees = POST['high_knees']
            dailytasks.plank_jumps = POST['plank_jumps']
            dailytasks.pushups = POST['pushups']
            dailytasks.squats = POST['squats']
            dailytasks.climbers = POST['climbers']
            dailytasks.knee_pull_ins = POST['knee_pull_ins']
            dailytasks.cross_crunches = POST['cross_crunches']
            return dailytasks.save()
        except DailyTasks.DoesNotExists:
            # Does not exist so lets create
            dailytasks = DailyTasks(user=user, **POST)
            return dailytasks.save()

    class Meta:
        model = DailyTasks
        fields = ['jumpjacks', 'high_knees', 'plank_jumps', 
                  'pushups', 'squats', 'climbers', 'knee_pull_ins', 
                  'cross_crunches', 'date']
        labels = {
            # Cardio
            'jumpjacks': _('Jumping Jacks'),
            'high_knees': _('High Knees'),
            'plank_jumps': _('Plank Jumps'),
            
            # Upper and Lower Body
            'pushups': _('Push Ups'),
            'squats': _('Squats'),
            
            # Abs
            'climbers': _('Mountain Climbers'),
            'knee_pull_ins': _('Knee Pull-Ins'),
            'cross_crunches': _('Cross Crunches'),
        }

class LinkAccountForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    def is_valid(self):
        valid = super(LinkAccountForm, self).is_valid()
        
        if not valid:
            return valid
        
        # Validate the given DSP account and password
        q = """SELECT id, login FROM accounts 
               WHERE password=PASSWORD('{0}')""".format(
               self.cleaned_data['password']
            )
        account = Accounts.objects.using('darkstar').raw(q) 
        if len(list(account)) == 0:
            self._errors['invalid_credentials'] = 'Either the account name and/or password are incorrect.'
            return False
        else: 
            self.account = account[0]
 
        return True

    def save(self, user, POST):
        try:
            linked_account = LinkedAccount(
                user=user, 
                acc_id=self.account.id, 
                name=self.account.login
            )
            
            return linked_account.save()
        except IntegrityError:
            self._errors['save_failed'] = 'Failed to save the account to the database'
            return False

class CharacterUpgradeForm(forms.Form):
    def get_job_levels(self):
        cursor = connections['darkstar'].cursor()
        q = """SELECT `war`, `mnk`, `whm`, `blm`, `rdm`, `thf`, `pld`, `drk`, `bst`, 
                      `brd`, `rng`, `sam`, `nin`, `drg`, `smn`, `blu`, `cor`, `pup`, 
                      `dnc`, `sch`, `geo`, `run` 
               FROM char_jobs WHERE charid={0} LIMIT 1""".format(self.charid)
        cursor.execute(q)
        desc = cursor.description
        return [
                OrderedDict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()
        ][0]
    
    
    def get_jobs(self):
        job_levels = self.get_job_levels()
        jobs = []
        for job, level in job_levels.items():
            if int(level) > 0:
                jobs.append((JOB_BY_NAME[job], JOB_NAMES[job]))
        
        return jobs

    def __init__(self, *args, **kwargs):
        self.charid = kwargs.pop('charid')
        super(CharacterUpgradeForm, self).__init__(*args, **kwargs)
        self.fields['jobs'] = forms.ChoiceField(
            label = "Select Job To Level",
            choices=self.get_jobs(),
            required = True,
        )
        
        self.fields['new_level'] = forms.IntegerField(
            label = "Level To Upgrade To",
            required = True,
        )
        self.helper = FormHelper()
        self.helper.form_id = 'id-chracterupgrade'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_character'
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Level Up!'))

class EnhancedSignetUpgrade(forms.Form):
    
    def __init__(self, *args, **kwargs):
        self.charid = kwargs.pop('charid')
        super(EnhancedSignetUpgrade, self).__init__(*args, **kwargs)
        self.fields['signet'] = forms.ChoiceField(
            label = "Select Buff To Upgrade",
            choices = SIGNET_CHOICES,
            required = True,
        )
        
        self.fields['upgrade'] = forms.IntegerField(
            label = "Level",
            required = True,
        )
        self.helper = FormHelper()
        self.helper.form_id = 'id-signetupgrade'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_signet'
        css = 'col-sm-6'
        self.helper.layout = Layout(
            Div(
                Div('signet', css_class="col-sm-12"),
                css_class="row"
            ),
            Div(
                Div('upgrade', css_class="col-sm-4"),
                Div(Button('qtyminus', '-', css_class='btn-md btn-info'), css_class="col-sm-1"),
                Div(Button('qtyplus', '+', css_class='btn-md btn-info'), css_class="col-sm-1"),
                css_class="row"
            ),
            Div( 
                Div(
                    Submit('submit', 'Upgrade!', css_class='btn-md'
                ), css_class='col-sm-2'),
                css_class='row submit_buttons'
            )
        )
