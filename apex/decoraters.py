import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
import pandas as pd
from django.contrib.auth import authenticate, logout, login
from .tests import PDF, Fetch_Data
from django_celery_beat.models import PeriodicTask, PeriodicTasks, IntervalSchedule
# this decorator checks for authenticated users
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user_raw_material')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func
# def admin_access(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         us = request.user.groups.all()[0].name
#         print(us)
#         return view_func(request, *args, **kwargs)
#     return wrapper_func
# this decorator is for access functionality of groups
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # print('working',allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('user_raw_material')
        return wrapper_func
    return decorator

# this decorator checks for active users
def unautherized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        try:
            user_id = request.user
            rg = Register.objects.filter(user__exact=user_id)
        except:
            redirect('login')
        # rs = rg.values()[0]
        try:
            rs = rg.values()[0]
            rs_status = rs['userRole']
            if rs_status == 'Active':
                return view_func(request,*args, **kwargs)
            else:
                # return view_func(request,*args, **kwargs)
                # print('nothing')
                return 'nothing'
        except:
            return view_func(request,*args, **kwargs)
    return wrapper_func
        
# this decorator checks for delete access
def del_access(view_func):
    def wrapper_func(request, *args, **kwargs):
        try:
            user_id = request.user
            rg = Register.objects.filter(user__exact=user_id)
        except:
            redirect('login')
        # rs = rg.values()[0]
        try:
            rs = rg.values()[0]
            rs_del = rs['delete_access']
            if rs_del == 'Yes':
                return view_func(request,*args, **kwargs)
            else:
                # return view_func(request,*args, **kwargs)
                # print('nothing')
                return 'nothing'
        except:
            return view_func(request,*args, **kwargs)
    return wrapper_func
