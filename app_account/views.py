import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from .models import User, Agreement
from app_account.forms import AgreementForm, AditionalInfoForm
from .decorators import deco
from django.urls import reverse

from django.http import HttpResponse
from django.core import serializers


#index view
@login_required
@deco
def index_view(request):
    user_data = User.objects.get(id=request.user.id)
    request.session['parent'] = user_data.parent
    request.session['router'] = user_data.router
    context = {
        'data': request.session['parent'],
        'user': user_data
    }
    return render(request, 'app_account/index.html', context)


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
        test = Agreement()
        selected_value = request.POST.keys()
        # print(selected_value)
        for item in selected_value:
            print(item)

        test.term_agreement = True
        test.private_agreement = True
        test.user = request.user
        test.save()
        print(test)

        if user_info.parent:
            print('parent')
            return redirect('index')
        else:
            print('child')
            return reverse("additional", kwargs={"id": request.user.id})


    agreement_form = AgreementForm()
    context = {
        'form': agreement_form,
    }
    return render(request, 'app_account/agreement.html',context)


class AgreementView(CreateView):
    model = Agreement
    context_object_name = 'form'
    form_class = AgreementForm
    template_name = 'app_account/agreement.html'
    # success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        data = Agreement.objects.filter(id=request.user.id).count()
        if request.user.is_authenticated and data == 0:
            return super(AgreementView, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        form.instance.id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        #최초 학부모 등록 관련 로직 넣기

        target = Agreement.objects.get(id=self.request.user.id)
        target.user = self.request.user
        target.save()
        if self.request.user.parent:
            return redirect('index')
        else:
            return reverse("additional", kwargs={"id": self.request.user.id})



#추가정보
class AdditionalCreateView(UpdateView):
    model = User
    context_object_name = 'form'
    form_class = AditionalInfoForm
    template_name = 'app_account/additional_info.html'
    success_url = '/'
    pk_url_kwarg = 'id'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.id == self.get_object().id:
            return super(AdditionalCreateView, self).dispatch(request, *args, **kwargs)
        elif request.user.parent and request.user.router == self.get_object().router:
            return super(AdditionalCreateView, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        birthday = self.get_object().birthday
        str_year = str(birthday).split('-')
        year = int(str_year[0])
        str_now = str(datetime.datetime.now()).split('-')
        now_year = int(str_now[0])
        calc = now_year - year + 1
        print(calc)
        context['year'] = calc
        return context
    # def get_queryset(self):


    #User.objects.create_user('navio',None,'tedsdcds1')
