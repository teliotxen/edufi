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
        'term/',
        views.AgreementView.as_view(),
        name='agreement'
    ),
    path(
        'user_info/<int:id>/',
        views.AdditionalCreateView.as_view(),
        name='additional'
    ),
    path(
        'term_update/<int:pk>/',
        views.AgreementUpdateView.as_view(),
        name='agreement_update'
    ),







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)