from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def login(request):
    params = {}
    params.update(csrf(request))
    return render_to_response('login.html', params)


def auth_check(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect('/accounts/invalid')
    else:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid.html')


def add(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            params = {}
            params.update(csrf(request))
            params['form'] = form
            return render_to_response('add.html', params)

    params = {}
    params.update(csrf(request))
    params['form'] = UserCreationForm()
    return render_to_response('add.html', params)
