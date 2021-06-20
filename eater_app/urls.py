from django.urls import path
from . import views

urlpatterns=[
    path('', views.dashboard),
    path('reserve', views.reserve),
    path('add', views.add),
    path('create', views.create),
    path('view/<int:res_id>', views.view),
    path('reserve/<int:res_id>', views.reservation),
    path('reserve/<int:res_id>/complete', views.complete),


]