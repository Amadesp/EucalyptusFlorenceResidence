from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    path('contacte-nos', views.Enviar_Email_Contact, name='contacte-nos'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('register',views.Register, name='register'),
    path('quartos', views.Quartos, name='quartos'),
    path('restaurante', views.Restaurante, name='restaurante'),
    path('jardim-infantil', views.Jardim_infantil, name='jardim-infantil'),
    path('piscina', views.Piscina, name='piscina'),
    path('auditorio', views.Auditorio, name='auditorio'),
    path('jardim', views.Jardim, name='jardim'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)