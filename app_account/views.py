from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from app_account.forms import AgreementForm, AditionalInfoForm
from .decorators import deco
from django.urls import reverse
from .models import User, Agreement
from .funcs import school_year_cal
from django.http import HttpResponse
from django.core import serializers


#index view
@login_required
@deco
def index_view(request):
    user_data = User.objects.get(id=request.user.id)
    router_user = User.objects.filter(router=user_data.router)
    children = router_user.filter(parent=False)

    request.session['parent'] = user_data.parent
    request.session['router'] = user_data.router
    context = {
        'data': request.session['parent'],
        'user': user_data,
        'router': children,
    }
    return render(request, 'app_account/index.html', context)


#profile view
@login_required
def profile_view(request, **kwargs):
    context = dict()
    context['kwargs'] = request.user.username
    return render(request, 'app_account/profile.html', context)


class AgreementView(CreateView):
    model = Agreement
    context_object_name = 'form'
    form_class = AgreementForm
    template_name = 'app_account/agreement.html'

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
        #최초 학부모 등록 관련 로직
        user_info = User.objects.get(id=self.request.user.id)
        if user_info.router is None:
            # 라우터 정보 가져오는 함수
            router_id = '12345'
        else:
            router_id = user_info.router

        router_sorted = User.objects.filter(router=router_id)
        init_user = router_sorted.filter(parent=True).count()
        print(init_user)
        if init_user == 0:
            user_info.parent = True
            user_info.save()

        target = Agreement.objects.get(id=self.request.user.id)
        target.user = self.request.user
        target.save()

        if user_info.parent:
            return reverse('index')
        else:
            return reverse("additional", kwargs={"id": self.request.user.id})


class AgreementUpdateView(UpdateView):
    model = Agreement
    context_object_name = 'form'
    form_class = AgreementForm
    template_name = 'app_account/agreement.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.id == self.get_object().id:
            return super(AgreementUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_object(self, queryset=None):
        pk_url_kwarg = Agreement.objects.filter(user=self.request.user)[0]
        return pk_url_kwarg

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
        if self.get_object().birthday is not None:
            birthday = self.get_object().birthday
            context['year'] = school_year_cal(birthday)
        return context


    #User.objects.create_user('navio',None,'tedsdcds1')




