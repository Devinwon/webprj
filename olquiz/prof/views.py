from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, StudentRegistrationForm
from .models import StudentProfile, TeacherProfile
from prof.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            sp = StudentProfile(user=user)
            sp.save()
            email = form.cleaned_data['email']
            user_name = form.cleaned_data['username']
            #print "i m here"
            return HttpResponseRedirect('/success/')
    else:
        form = StudentRegistrationForm()
        variables = RequestContext(request, {
        	'form': form
        	})
 
    return render_to_response(
    'registration/register.html',
    variables,
    ) 

def register_success(request):
    # print "is now success"
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
# @login_required
def home(request): 
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )


def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            TP = TeacherProfile(user=user)
            #print "i m here"
            TP.save()            
            return HttpResponseRedirect('/success')
    args = {}
    # args.update(csrf(request))
    args['form'] = TeacherRegistrationForm()
    print args
    return render(request, 'registration/teacherregister.html', args)