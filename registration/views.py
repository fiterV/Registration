from django.shortcuts import render, HttpResponse, reverse, Http404, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        formReg = RegisterForm()
        context  = {
            'form':form,
            'formReg':formReg,
        }
        return render(request, "registration/index.html", context)

def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    print(user)
    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('registration:indexView'))
        else:
            return HttpResponse("User is not active")
    else:
        if User.objects.filter(username=username).exists():
            return HttpResponse('Wrong password')
        return HttpResponse("Invalid login details")

def registerUser(request):
    formReg = RegisterForm(request.POST, request.FILES or None)#user profile
    form = LoginForm(request.POST)
    if formReg.is_valid() and form.is_valid():
        user = form.save()
        user.set_password(user.password)
        user.save()
        profile = formReg.save(commit=False)
        profile.user = user

        if 'picture' in request.FILES:
            profile.picture = request.FILES['picture']
            print(profile.picture)

        profile.save()
        login(request, user)
        return HttpResponseRedirect(reverse('registration:indexView'))

    else:
        return HttpResponse(str(form.errors))

@login_required
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('registration:indexView'))