from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from accounts.token import account_activation_token
from django.core.mail import send_mail,send_mass_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from django.shortcuts import HttpResponse
from django.conf import settings

import os
import re
import uuid




def send_account_confirmation_email(request, user):
    current_site = get_current_site(request)
    subject = 'Markazun Nahda user account'
    message = render_to_string('accounts/acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    user.email_user(subject, message)


