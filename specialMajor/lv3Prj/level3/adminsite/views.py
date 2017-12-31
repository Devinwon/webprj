from django.shortcuts import render

# Create your views here.

def userdetail(request):
    return render(request,'userDetail.html',{})

def userListPanel(request):
    return render(request,'userListPanel.html',{})

def userListLogin(request):
    return render(request,'userListPanelLogin.html',{})


# 逻辑代码，不可用
# def createuser(request):
#     user = CreateUserFrom.save()
#     up = UserProfile(belong_to=user)
#     up.save()