from functools import wraps
from django.shortcuts import redirect
from django.template.response import TemplateResponse


def check_user_perm(func):
    """
    - 로그인 안했으면 로그인화면으로 돌려보낸다.
    - 유저 검사해서 어드민 권한 없으면 권한없다고 알려주는 페이지로 보낸다.
    """

    def wrapper(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        if not user.is_admin:
            data = {'error': 'NOT_ADMIN', 'message': '관리자 권한이 없어 접근이 불가능합니다.'}
            return TemplateResponse(
                request,
                '<template_name>',
                {'data': data}
            )
        return func(request, *args, **kwargs)

    return wrapper


def deco(func):
    def decorator(request, *args, **kwargs):

        user = request.user
        print(user)
        print("%s %s" % (func.__name__, "before"))
        result = func(request, *args, **kwargs)
        print("%s %s" % (func.__name__, "after"))
        result.set_cookie('test', 'text', max_age=300000 )
        return result
    return decorator



