from django.contrib import admin
from django.urls import path
from app_account import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index'),
    path(
        'profile/<int:user_id>/',
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
    path(
        'router/<int:id>/',
        views.RouterUpdateView.as_view(),
        name='router'
    ),
    path(
        'parents/',
        views.add_parents,
        name = 'add_parents'
    ),
    path(
        'report/<int:user_id>/',
        views.ReportListView.as_view(),
        name='report'
    ),
    path(
        'report_detail/<int:sheets_id>/',
        views.ReportDetailView.as_view(),
        name='report_detail'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)