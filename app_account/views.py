from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.core import serializers
from allauth.account.views import SignupView
# Create your views here.
from app_account.forms import AgreementForm

def deco(func):
    def decorator(*args, **kwargs):
        # if request.COOKIES['test']:
        #     print('cookie')
        # else:
        #     print('none')
        print("%s %s" % (func.__name__, "before"))
        result = func(*args, **kwargs)
        print("%s %s" % (func.__name__, "after"))
        result.set_cookie('test', 'text', max_age=300000 )
        return result

    return decorator


#index view
@login_required
def index_view(request):

    return render(request, 'app_account/index.html')


#profile view

@login_required
def profile_view(request, **kwargs):
    # if request.session['parent']:
    #     print(True)
    # else:
    #     request.session['parent'] = True
    #     parent_count = User.objects.filter(parent=True).count()
    #     if parent_count == 0:
    #         print(1)
    # print(request.session['parent'])
    context = dict()
    context['kwargs'] = request.user.username
    return render(request, 'app_account/profile.html', context)


#agreement_view

def agreement_view(request):
    #초기 실행
    user_info = User.objects.get(id=request.user.id)
    if user_info.router is None:
        #라우터 정보 가져오는 함수
        router_id = '12345'
    else:
        router_id = user_info.router

    router_sorted = User.objects.filter(router=router_id)
    init_user = router_sorted.filter(parent=True).count()
    print(init_user)
    if init_user == 0:
        user_info.parent = True
        user_info.save()



    #post
    if request.POST:
        agreement_form = AgreementForm(request.POST)
        if user_info.parent:
            print('parent')
            return redirect('index')
        else:
            print('child')
            return redirect('additional')

    agreement_form = AgreementForm()
    context = {
        'form': agreement_form,
    }

    return render(request, 'app_account/agreement.html',context)


#추가정보
def additional_info(request):
    if request.POST:
        return redirect('index')
    return render(request, 'app_account/additional_info.html')



    #User.objects.create_user('navio',None,'tedsdcds1')
