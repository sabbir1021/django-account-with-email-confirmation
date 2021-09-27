from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from accounts.forms import RegisterForm
from django.views import View, generic
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()
#token import
from accounts.utils.email import send_account_confirmation_email
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode    
from accounts.token import account_activation_token


def home(request):
    return render(request, 'accounts/home.html')

class RegisterView(generic.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    def form_valid(self, form):
        user = form.save()
        send_account_confirmation_email(self.request, user)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    def get_success_url(self):
        next_url = self.request.POST.get('next', None)
        if next_url:
            return "%s" % (next_url)
        else:
            return reverse_lazy('accounts:login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64)).decode('utf-8')
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.email_confirmed = True
        user.save()
        return redirect('accounts:login')
    else:
        return redirect('accounts:login')
