from django.conf.urls import *
from django.views.generic.base import TemplateView

from registration.forms import RegistrationFormTermsOfService
from invitation.views import invite, invited, register

urlpatterns = patterns('',
    url(r'^invite/complete/$',
                TemplateView.as_view(
                    template_name='invitation/invitation_complete.html'),
                name='invitation_complete'),
    url(r'^invite/$',
                invite,
                name='invitation_invite'),
    url(r'^invited/(?P<invitation_key>\w+)/$', 
                invited,
                name='invitation_invited'),
    url(r'^register/$',
                register,
                { 'backend': 'registration.backends.default.DefaultBackend' },
                name='registration_register'),
)
