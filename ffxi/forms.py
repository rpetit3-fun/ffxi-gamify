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

from darkstar.models import Chars
from ffxi.form_constants import *
from ffxi.models import DailyTasks, LinkedAccount, ExperienceStats
from darkstar.models import Accounts, CharVars

class RegistrationFormWithName(RegistrationFormUniqueEmail):
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

class DailyTasksForm(forms.ModelForm):
    estimated_exp = forms.CharField(
        label = "Estimated EXP Gain",
    )

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

        
        self.helper.layout = Layout(
            Div(
                'jumpjacks', 'high_knees', 'plank_jumps', 'pushups', 
                'estimated_exp',
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
        fields = ['jumpjacks', 'high_knees', 'plank_jumps', 'pushups', 'squats',
                  'climbers', 'knee_pull_ins', 'cross_crunches', 'date']
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
    
    def __init__(self, *args, **kwargs):
        super(LinkAccountForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'link-account'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_account'

        self.helper.add_input(Submit('submit', 'Link Account!', css_class='btn-md pull-right level-submit'))
    
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
            # Check if more that two accounts exists
            if LinkedAccount.objects.filter(user=user).count() < 3:
                exp = ExperienceStats.objects.get(user=user)
                exp.exp = exp.exp + 100000
                exp.save()
                
            linked_account = LinkedAccount(
                user=user, 
                acc_id=self.account.id, 
                name=self.account.login
            )
            linked_account.save()

            cursor = connections['darkstar'].cursor()
            q = """SELECT charid, charname FROM chars 
                   WHERE accid={0} LIMIT 1""".format(self.account.id)
            cursor.execute(q)
            character = cursor.fetchone()
            if len(character) == 0:
                return [False, linked_account]
            else:
                return [True, {'charid':character[0], 'charname':character[1]}]
        except IntegrityError:
            self._errors['save_failed'] = 'Failed to save the account to the database'
            return [False]
            


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
                jobs.append((job, JOB_NAMES[job]))
        
        return jobs

    def is_valid(self, user):
        valid = super(CharacterUpgradeForm, self).is_valid()
        
        if not valid:
            return valid
        
        # Validate user has enough EXP to spend
        exp = ExperienceStats.objects.get(user=user)
        self.cleaned_data['char_cost'] = self.cleaned_data['char_cost'].replace(",", "")
        if exp.exp < int(self.cleaned_data['char_cost']):
            self._errors['not_enough_exp'] = 'You do not have enough stored EXP to make that upgrade.'
            return False

        return True

    def save(self, user):
        try:
            # Deduct EXP Cost
            exp = ExperienceStats.objects.get(user=user)
            exp.exp = exp.exp - int(self.cleaned_data['char_cost'])
            exp.save()
            
            # Increase level
            cursor = connections['darkstar'].cursor()
            q = """UPDATE `char_jobs` SET `{0}`={1} 
                   WHERE `charid`={2}""".format(
                   self.cleaned_data['jobs'], 
                   self.cleaned_data['level'], 
                   self.charid
            )
            cursor.execute(q)
            
            return exp.exp
        except IntegrityError:
            self._errors['save_failed'] = 'Failed to save the upgrade to the database'
            return False
            
    def __init__(self, *args, **kwargs):
        self.charid = kwargs.pop('charid')
        super(CharacterUpgradeForm, self).__init__(*args, **kwargs)
        self.fields['jobs'] = forms.ChoiceField(
            label = "Select Job To Level",
            choices=self.get_jobs(),
            required = True,
        )
        
        self.fields['level'] = forms.IntegerField(
            label = "Increase Level (Max 75 or Genkai)",
            required = True,
        )
        
        self.fields['start_level'] = forms.IntegerField()
        
        self.fields['char_cost'] = forms.CharField(
            label = "Estimated Cost",
        )
        self.fields['char_exp'] = forms.CharField(
            label = "Remaining EXP",
        )
        
        self.helper = FormHelper()
        self.helper.form_id = 'character-upgrade'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_character'
        self.helper.layout = Layout(
            Div(
                Div('jobs', css_class="col-sm-12"),
                css_class="row"
            ),
            Div(
                FieldWithButtons(
                    'level', 
                    StrictButton('-', name='qtyminus', css_class='btn-md btn-info level-down'),
                    StrictButton('+', name='qtyplus', css_class='btn-md btn-info level-up'),
                    css_class="col-sm-6"
                ),
                Div('char_cost', css_class="col-sm-3"),
                Div('char_exp', css_class="col-sm-3"),
                Field('start_level', type="hidden"),
                css_class="row"
            ),
            Div( 
                Div(
                    Submit('submit', 'Level Up!!', css_class='btn-md pull-right level-submit'
                ), css_class='col-sm-12'),
                css_class='row submit_buttons'
            )
        )
        

class EnhancedSignetUpgrade(forms.Form):
    def is_valid(self, user):
        valid = super(EnhancedSignetUpgrade, self).is_valid()
        
        if not valid:
            return valid
        
        # Validate user has enough EXP to spend
        exp = ExperienceStats.objects.get(user=user)
        self.cleaned_data['signet_cost'] = self.cleaned_data['signet_cost'].replace(",", "")
        if exp.exp < int(self.cleaned_data['signet_cost']):
            self._errors['not_enough_exp'] = 'You do not have enough stored EXP to make that upgrade.'
            return False

        return True
    
    def save(self, user):
        try:
            # Deduct EXP Cost
            exp = ExperienceStats.objects.get(user=user)
            exp.exp = exp.exp - int(self.cleaned_data['signet_cost'])
            exp.save()
            
            # Increase buff level
            cursor = connections['darkstar'].cursor()
            q = """INSERT INTO `char_vars` (`charid`, `varname`, `value`)
                   VALUES ('{0}', '{1}', '{2}')
                   ON DUPLICATE KEY UPDATE `value`={2}""".format(
                   self.charid,
                   self.cleaned_data['signet'], 
                   self.cleaned_data['upgrade']
            )
            cursor.execute(q)
            

            return exp.exp
        except IntegrityError:
            self._errors['save_failed'] = 'Failed to save the upgrade to the database'
            return False
    
    def __init__(self, *args, **kwargs):
        self.charid = kwargs.pop('charid')
        super(EnhancedSignetUpgrade, self).__init__(*args, **kwargs)
        self.fields['signet'] = forms.ChoiceField(
            label = "Select Buff To Upgrade",
            choices = SIGNET_CHOICES,
            required = True,
        )
        
        self.fields['upgrade'] = forms.IntegerField(
            label = "Buff Level (Max 30)",
            required = True,
        )
        
        self.fields['start_upgrade'] = forms.IntegerField()
        
        self.fields['signet_cost'] = forms.CharField(
            label = "Estimated Cost",
        )
        self.fields['signet_exp'] = forms.CharField(
            label = "Remaining EXP",
        )

        self.helper = FormHelper()
        self.helper.form_id = 'signet-upgrade'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_signet'

        self.helper.layout = Layout(
            Div(
                Div('signet', css_class="col-sm-12"),
                css_class="row"
            ),
            Div(
                FieldWithButtons(
                    'upgrade', 
                    StrictButton('-', name='qtyminus', css_class='btn-md btn-info buff-down'),
                    StrictButton('+', name='qtyplus', css_class='btn-md btn-info buff-up'),
                    css_class="col-sm-6"
                ),
                Div('signet_cost', css_class="col-sm-3"),
                Div('signet_exp', css_class="col-sm-3"),
                Field('start_upgrade', type="hidden"),
                css_class="row"
            ),
            Div( 
                Div(
                    Submit('submit', 'Upgrade!', css_class='btn-md pull-right upgrade-submit'
                ), css_class='col-sm-12'),
                css_class='row submit_buttons'
            )
        )
