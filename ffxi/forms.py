from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from registration.forms import RegistrationFormUniqueEmail

from ffxi.models import DailyTasks

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
