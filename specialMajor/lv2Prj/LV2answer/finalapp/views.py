from django.shortcuts import render, redirect,  render_to_response
from finalapp.models import Video, Ticket, UserProfile, Collection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from finalapp.form import ChangeForm, ChangepwdForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login
# Create your views here.
def listing(request, cate=None):
    context = {}

    if cate == 'editors':
        vids_list = Video.objects.filter(editors_choice=True)
    else:
        vids_list = Video.objects.all()

    page_robot = Paginator(vids_list, 6)
    page_num = request.GET.get('page')
    try:
        vids_list = page_robot.page(page_num)
    except EmptyPage:
        vids_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        vids_list = page_robot.page(1)

    try:
        user = UserProfile.objects.get(username=request.user.user.username)
        context['user'] = user
    except:
        pass

    context['vids_list'] = vids_list
    return render(request, 'listing.html', context)

def index_login(request):
    context = {}
    if request.method == "GET":
        form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to="list")
    context['form'] = form
    return render(request, 'register_login.html', context)

def index_register(request):
    context = {}
    if request.method == "GET":
        form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form'] = form
    return render(request, 'register_login.html', context)

def detail(request, id):
    context = {}

    vid_info = Video.objects.get(id=id)
    voter_id = request.user.id
    like_counts = Video.objects.get(id=id).likes
    try:
        user_ticket_for_this_video = Ticket.objects.get(voter_id=voter_id, video_id=id)
        context['user_ticket'] = user_ticket_for_this_video
    except:
        pass

    try:
        user = UserProfile.objects.get(username=request.user.user.username)
        context['user'] = user
    except:
        pass

    context['like_counts'] = like_counts
    context['vid_info'] = vid_info
    return render(request, 'detail.html', context)

def vote(request, id):
    if not isinstance(request.user, User):
        return redirect(to="detail", id=id)
    voter_id = request.user.id
    try:
        user_ticket_for_this_video = Ticket.objects.get(voter_id=voter_id, video_id=id)
        user_ticket_for_this_video.choice = request.POST["vote"]
        user_ticket_for_this_video.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, video_id=id, choice=request.POST["vote"])
        new_ticket.save()

    if request.POST["vote"] == "like":
        video = Video.objects.get(id=id)
        video.likes += 1
        video.save()
    if request.POST["vote"] == "dislike":
        video = Video.objects.get(id=id)
        video.likes -= 1
        video.save()

    return redirect(to="detail", id=id)

def myinfo(request, username):
    if not isinstance(request.user, User):
        return redirect(to="list")

    try:
        user = User.objects.get(username=username)
    except:
        return redirect(to="list")

    if str(user) == str(request.user.username):
        context = {}
        if request.method == 'GET':
            form = ChangeForm

        if request.method == 'POST':
            form = ChangeForm(request.POST, request.FILES)

            if form.is_valid():
                name = form.cleaned_data["修改姓名"]
                sex = form.cleaned_data['性别']
                img = form.cleaned_data["修改头像"]
                user_new_profile = UserProfile(username=name, sex=sex, avatar=img, belong_to=user)

                try:
                    user_old_profile = UserProfile.objects.get(username=request.user.user.username)
                except ObjectDoesNotExist:
                    user_old_profile = False

                if user_old_profile:
                    user_old_profile.delete()

                user_new_profile.save()
                return redirect(to="myinfo", username=username)

        context['form'] = form
        return render(request, 'myinfo.html', context)
    else:
        return redirect(to="list")

def mycollection(request, username):
    if not isinstance(request.user, User):
        return redirect(to='list')

    try:
        user = User.objects.get(username=username)
    except:
        return redirect(to='list')

    if str(user) == str(request.user.username):
        context = {}

        liker = User.objects.get(username=username)
        # collection_list = Collection.objects.filter(liker=liker)
        collection_list = Ticket.objects.filter(choice='like')
        print(collection_list,len(collection_list))

        page_robot = Paginator(collection_list, 3)
        page_num = request.GET.get('page')
        try:
            collection_list = page_robot.page(page_num)
        except EmptyPage:
            collection_list = page_robot.page(page_robot.num_pages)
        except PageNotAnInteger:
            collection_list = page_robot.page(1)

        context['collection_list'] = collection_list
        return render(request, 'mycollection.html', context)
    else:
        return redirect(to='list')

def changepwd(request, username):
    if not isinstance(request.user, User):
        return redirect(to='list')

    try:
        user = User.objects.get(username=username)
    except:
        return redirect(to='list')

    if str(user) == str(request.user.username):
        context = {}
        if request.method == 'GET':
            form = ChangepwdForm
            context['form'] = form
            return render(request, 'changepwd.html', context)
        else:
            form = ChangepwdForm(request.POST)
            if form.is_valid():
                username = request.user.username
                oldpassword = request.POST.get('oldpassword', '')
                user = authenticate(username=username, password=oldpassword)
                if user:
                    newpassword = request.POST.get('newpassword1', '')
                    user.set_password(newpassword)
                    user.save()
                    login(request, user)
                    return redirect(to="myinfo", username=username)
                else:
                    return redirect(to='relogin')
            else:
                context['form'] = form
                return render(request, 'changepwd.html', context)
    else:
        return redirect(to='list')
