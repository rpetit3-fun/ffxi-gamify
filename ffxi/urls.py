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
    url(r'^ajax/add-exp-chain/', 'ffxi.ajax.add_exp_chain', name='add_exp_chain'),
    url(r'^ajax/get-signet-cost/', 'ffxi.ajax.get_signet_cost', name='get_signet_cost'),
    url(r'^ajax/get-level-cost/', 'ffxi.ajax.get_level_cost', name='get_level_cost'),
    url(r'^ajax/get-max-level/', 'ffxi.ajax.get_max_level', name='get_max_level'),

    # ffxi-gamify:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ffxi.views.index', name='home'),
    url(r'^daily-tally/', 'ffxi.views.daily_tally', name='daily_tally'),
    url(r'^link-account/', 'ffxi.views.link_account', name='link_account'),
    url(r'^record-feats/', 'ffxi.views.record_feats', name='record_feats'),
    url(r'^ub3r1337-rank/', 'ffxi.views.ub3r1337_rank', name='ub3r1337_rank'),
    url(r'^character/(?P<charid>\d+)/(?P<charname>.+)/$', 'ffxi.views.character', name='character'),

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
