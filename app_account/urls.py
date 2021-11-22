from django.contrib import admin
from django.urls import path
from app_account import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index'),
    path(
        'profile/<str:user_id>/',
        views.profile_view,
        name='profile'
    ),
    path(
        'agreement/',
        views.agreement_view,
        name='agreement'
    ),
    path(
        'additional/',
        views.additional_info,
        name='additional'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)