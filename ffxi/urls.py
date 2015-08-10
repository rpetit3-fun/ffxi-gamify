from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from registration.backends.default.views import RegistrationView, ActivationView
from django_email_changer.views import CreateUserEmailModificationRequest, ActivateUserEmailModification, \
    ActivationEmailSentSuccessView

from ffxi.forms import RegistrationFormWithName

urlpatterns = [

    # AJAX
    url(r'^ajax/get-daily-stats/', 'ffxi.ajax.get_daily_stats', name='get_daily_stats'),
    url(r'^ajax/update-steps/', 'ffxi.ajax.update_steps', name='update_steps'),
    
    # ffxi-gamify:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ffxi.views.index', name='home'),
    url(r'^daily-tasks/', 'ffxi.views.daily_tasks', name='daily_tasks'),
    url(r'^missions/', 'ffxi.views.missions', name='missions'),
    url(r'^quests/', 'ffxi.views.quests', name='quests'),
    url(r'^rewards/', 'ffxi.views.rewards', name='rewards'),
    
    # django-email-changer
    url(r'accounts/email/change/activate/(?P<code>[^/]+)/',
        ActivateUserEmailModification.as_view(),
        name="django_change_email_activate_new_email"),
    url(r'^accounts/email/change/sent/$',
        ActivationEmailSentSuccessView.as_view(),
        name="django_change_email_sent_activation_email"),
    url(r'^accounts/email/change/$',
        CreateUserEmailModificationRequest.as_view(),
        name="django_email_changer_change_view"),
    
    # django-registration
    url(r'^accounts/$', RedirectView.as_view(url='/', )),
    # Fix for password reset
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),
    url(r'^accounts/password/reset/confirm/$',
        RedirectView.as_view(url='/', )),
    url(r'^accounts/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect': '/accounts/password/reset/done/'},
        name="password_reset"),
    url('^accounts/activate/$', ActivationView.as_view(),
        {'activation_key': 'None'},
        name='registration_activate'),
    # enable unique email registration feature
    url(r'^accounts/register/$',
        RegistrationView.as_view(form_class=RegistrationFormWithName),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
