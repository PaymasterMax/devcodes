from django.urls import path, include
from . import views
from django.conf.urls import url
urlpatterns = [
    url('', views.index, name='index'),
    url('daraja/stk-push/', views.stk_push_callback, name='mpesa_stk_push_callback'),
]
