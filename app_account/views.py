from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from app_account.forms import AgreementForm, AditionalInfoForm, RouterForm
from .decorators import deco
from django.urls import reverse
from .models import User, Agreement, Router
from english.models import UserAnswer
from .funcs import school_year_cal, form_data_to_string
from .forms import UserForm
import json
from django.http import HttpResponse
from django.core import serializers


#결과 리스트 뷰
class ReportListView(ListView):
    model = UserAnswer
    template_name = 'app_account/report_list.html'
    context_object_name = 'user_answer'
    paginate_by = 8

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return UserAnswer.objects.filter(user_id=user_id).order_by("-dt_created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = get_object_or_404(User, id=self.kwargs.get('user_id'))
        return context


#결과 디테일 뷰
class ReportDetailView(DetailView):
    model = UserAnswer
    template_name = 'app_account/report_detail.html'
    pk_url_kwarg = 'sheets_id'
    context_object_name = 'answer_sheet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sheets_id = self.kwargs.get('sheets_id')
        context['report'] = UserAnswer.objects.get(id=sheets_id)
        return context


#index view
@login_required
def index_view(request):
    #사용자가 접속한 공유기 주소 고유 값 가져오기
    #공유기 주소 값으로 해당 공유기 주소에 있는 사용자 유무 파악
    #사용자 유무 파악 후 사용자가 없으면 signup + popup
    #사용자가 있으면 로그인 화면으로

    user_data = User.objects.get(id=request.user.id)

    try:
        router_user = User.objects.filter(router=user_data.router)
        children = router_user.filter(parent=False)
        router = Router.objects.get(router_id=user_data.router)
    except:
        return redirect('agreement')

    request.session['parent'] = user_data.parent
    request.session['router'] = user_data.router
    context = {
        'data': request.session['parent'],
        'user': user_data,
        'children': children,
        'router': router,
    }
    return render(request, 'app_account/index.html', context)


#profile view
@login_required
def profile_view(request, **kwargs):
    context = dict()
    context['user_id'] = request.user.id
    # return reverse("profile", kwargs={"user_id": request.user.id})
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
            return redirect('index') #term으로 다시 진입시 발생

    def form_valid(self, form):
        form.instance.id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        #최초 학부모 등록 관련 로직
        user_info = User.objects.get(id=self.request.user.id)
        if user_info.router is None:
            # 라우터 정보 가져오는 함수

            router_id = '111112'
            user_info.router = router_id
            user_info.save()

            try:
                router_information = Router.objects.create(router_id=router_id, max_time=180, free_time=[6,7])
            except:
                router_information = Router.objects.get(router_id=router_id)

        else:
            router_id = user_info.router
            router_information = Router.objects.get(id=router_id)

        router_sorted = User.objects.filter(router=router_id)
        init_user = router_sorted.filter(parent=True).count()
        if init_user == 0:
            user_info.parent = True
            user_info.save()
            self.request.session['initial'] = True
        else:
            self.request.session['initial'] = False

        target = Agreement.objects.get(id=self.request.user.id)
        target.user = self.request.user
        target.save()

        if user_info.parent:
            return reverse('router', kwargs={'id':router_information.id})
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


class RouterUpdateView(UpdateView):
    model = Router
    context_object_name = 'form'
    form_class = RouterForm
    template_name = 'app_account/router_update.html'
    success_url = '/'
    # pk_url_kwarg = 'id'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.router == self.get_object().router_id and self.request.user.parent:
            return super(RouterUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_object(self, queryset=None,):
        number = self.request.user.router
        pk_url_kwarg = Router.objects.get(router_id=number).id
        return get_object_or_404(self.model, id=pk_url_kwarg)


@login_required
def add_parents(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form_username = form_data_to_string(form['username'])
            form_password = form_data_to_string(form['password'])
            print(form_username, form_password)

            new_user = User.objects.create(
                username=form_username,
                parent=True
            )
            new_user.set_password(form_password)
            new_user.save()

    if User.objects.get(id=request.user.id).parent:
        return render(request, 'app_account/add_parents.html', {'form': form})
    else:
        return redirect('index')


