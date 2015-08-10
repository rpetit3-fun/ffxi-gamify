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
        self.fields['steps'].disabled = True
        self.helper.layout = Layout(
            Div(
                'steps', 'pushups',
                css_class=css
            ),
            Div(
                'situps', 'squats',
                Div(
                    Div(HTML('''
                                <button id="update_steps" type="button" class="btn btn-primary btn-lg">
                                    Sync Steps
                                </button>
                            '''), css_class='col-sm-5 col-sm-offset-3'),
                    Div(Submit('submit', 'Save', css_class='btn-lg'), css_class='col-sm-3'),
                    css_class='row submit_buttons'
                ),
                css_class=css
            ),
            Field('date', type='hidden'),
        )

    def save(self, user, POST):
        try:
            # Exists so lets update
            dailytasks = DailyTasks.objects.get(user=user, date=POST['date'])
            dailytasks.pushups = POST['pushups']
            dailytasks.situps = POST['situps']
            dailytasks.squats = POST['squats']
            return dailytasks.save()
        except DailyTasks.DoesNotExists:
            # Does not exist so lets create
            dailytasks = DailyTasks(user=user, **POST)
            return dailytasks.save()

    class Meta:
        model = DailyTasks
        fields = ['steps', 'pushups', 'situps', 'squats', 'date']
        labels = {
            'pushups': _('Push Ups <div id="id_pushups-icon"></div>'),
            'situps': _('Sit Ups <div id="id_situps-icon"></div>'),
            'squats': _('Squats <div id="id_squats-icon"></div>'),
            'steps': _('Steps <div id="id_steps-icon"></div>'),
        }
