from re import sub
from celery import shared_task
from django.db import IntegrityError, transaction
from django.core.mail import send_mail, EmailMessage
from datetime import date
import time
from .models import *
import datetime
from datetime import date
from .helper import *
import json
import requests
from django.conf import settings

#run code is: celery -A apexindustries.celery worker --loglevel=info --pool=solo,
# celery -A apexindustries beat -l info ,
# celery -A apexindustries purge

@shared_task
def timmer():
    with transaction.atomic():
        
        users = Register.objects.all()
        user_list = users.values()
        my_time = int(str(datetime.datetime.now())[11:13])
        if my_time >=8 and my_time <= 20:
            for i in user_list:
                user_name = i['UserName']
                status = i['userRole']
                user_id = i['user_id']
                get_user = Register.objects.get(user_id=user_id)
                get_user.userRole = 'Active'
                get_user.save()
                # print(get_user.userRole,get_user.UserName,'working hours')
        elif my_time > 20 or my_time < 8:
            for i in user_list:
                user_name = i['UserName']
                status = i['userRole']
                user_id = i['user_id']
                get_user = Register.objects.get(user_id=user_id)
                if user_name == 'admin@gmail.com':
                    get_user.userRole = 'Active'
                    get_user.save()
                else:
                    get_user.userRole = 'Not_Active'
                # print(get_user.userRole,get_user.UserName,'working hours over')
                    get_user.save()
        return 'done'

# Daily EOD a report in PDF format should be sent to a email of admin stating the details of RM arrived today,
# FM processed today and essential items used today.
# i need to fetch RM , FM, and ES data 
@shared_task
def daily_mail():
    pass
    # current_date = datetime.date.today()
    # RM_Data = rawMaterial.objects.filter(RM_Date__exact=current_date)
    # id_list = []
    # register_id = []
    # Date =[]
    # RM_thickness=[]
    # RM_Size = []
    # RM_Grade = []
    # RM_coilweight = []
    # RM_Scrapweight = []
    # for i in RM_Data.values():
    #     id_list.append(i['id'])
    #     register_id.append(i['register_id'])
    #     Date.append(i['RM_Date'])
    #     RM_thickness.append(i['RM_Thickness'])
    #     RM_Grade.append(i['RM_Grade'])
    #     RM_Size.append(i['RM_Size'])
    #     RM_coilweight.append(i['RM_coilWeight'])
    #     RM_Scrapweight.append(i['RM_scrapWeight'])
    # dic = {
    #     'id': id_list,
    #     'register id': register_id,
    #     'Date':Date,
    #     'Raw Material Thickness': RM_thickness,
    #     'Raw Material Grade': RM_Grade,
    #     'Raw Material Size': RM_Size,
    #     'Raw Material Coil Weight': RM_coilweight,
    #     'Raw Material ScrapeWeight': RM_Scrapweight
    # }            
    # df = pd.DataFrame(dic)
    # print(df)
    # body = 'body'
    # subject = 'subject'
    # sender_mail = 'shashank.singh@datenwissen.com'
    # email = EmailMessage(subject,body,'zombiebaloon@gmail.com',[sender_mail])
    # email.content_subtype='html'
    # email.send()

@shared_task
def weekly_reports():
    body = '##########################################'
    subject = 'subject'
    sender_mail = 'shashank.singh@datenwissen.com'
    email = EmailMessage(subject,body,'teamdwkaustubh@gmail.com',[sender_mail])
    email.content_subtype='html'
    # file = open("manage.py" , "r")
    # email.attach("manage.py",file.read(),'text/plain')
    email.send()

@shared_task
def Active_time():
    SetTimer(register=Register.objects.all())
    # if t >= a_t and t <= d_t:
    #     for i in user_list:
    #             user_id = i['user_id']
    #             get_user = Register.objects.get(user_id=user_id)
    #             get_user.userRole = 'Active'
    #             get_user.save()
    # elif t > d_t:
    #     for i in user_list:
    #             user_name = i['UserName']
    #             status = i['userRole']
    #             user_id = i['user_id']
    #             get_user = Register.objects.get(user_id=user_id)
    #             if user_name == 'admin@gmail.com':
    #                 get_user.userRole = 'Active'
    #                 get_user.save()
    #             else:
    #                 get_user.userRole = 'In-Active'
    #             # print(get_user.userRole,get_user.UserName,'working hours over')
    #                 get_user.save()
    # elif t < a_t:
    #     for i in user_list:
    #             user_name = i['UserName']
    #             status = i['userRole']
    #             user_id = i['user_id']
    #             get_user = Register.objects.get(user_id=user_id)
    #             if user_name == 'admin@gmail.com':
    #                 get_user.userRole = 'Active'
    #                 get_user.save()
    #             else:
    #                 get_user.userRole = 'In-Active'
    #             # print(get_user.userRole,get_user.UserName,'working hours over')
    #                 get_user.save()


# @shared_task
# def Inactive_time():
#     users = Register.objects.all()
#     user_list = users.values()
#     my_time = int(str(datetime.datetime.now())[11:13])
#     a_time = Timmer.objects.filter().last()
#     d_time = int(a_time.inactive_time)
#     # user_time = int(t_val['active_time'])
#     if my_time == d_time:
#         for i in user_list:
#                 user_name = i['UserName']
#                 status = i['userRole']
#                 user_id = i['user_id']
#                 get_user = Register.objects.get(user_id=user_id)
#                 get_user.userRole = 'Not_Active'
#                 get_user.save()
#     else:
#         print('no time given')

#     return 'done'


# this task will run every day around midnight to check if there is any zero entries registered in rm and fm table
# so that it can put zero data on that particular day, whole task is for overview rm and fm graph purpose
@shared_task
def check_for_data():
    today = date.today()
    rw = rawMaterial.objects.filter(RM_Date__year=today.year,
                                    RM_Date__month=today.month,).values()
    fm = FMstock.objects.filter(FM_Date__year=today.year).values()

    dic_weight = extracting_data_for_graph.dict_for_raw(
        dic=rw, key='RM_Date', value='RM_coilWeight')
    dic_scrap = extracting_data_for_graph.dict_for_raw(
        dic=rw, key='RM_Date', value='RM_scrapWeight')

    fm_weight = extracting_data_for_graph.dict_for_raw(
        dic=fm, key='FM_Date', value='FM_Weight')
    fm_scrap = extracting_data_for_graph.dict_for_raw(
        dic=fm, key='FM_Date', value='FM_scrapWeight')
    date = str(datetime.date.today())[8:]
    d = {'1':1,'2':3,'8':8}
    if date in d:
        pass
    else:
        d[date] = 0

    

@shared_task
def drive_backup():
    headers = {"Authorization": "Bearer ya29.a0ARrdaM_IU_tjgVtXTsalknni5IHXX0qRsS10HBlKhQntXXrhrcogNo5y63jNrJ0merJUFmHBqX4Em04CxvnXHwv56t5W5fp6SLQy8_tZNXHX0okzqzRHV7-S3slBoZNgWlFayjzPJYR2lCPCMXcwwGpHGu8O"}
    print("todays date = ", date.today())
    para = {
        "name": "Apex" + "__" + str(date.today()) + "__" + ".sqlite3",
        "parents": ['1aB_F97zfveBiCX3z2cFVlNB5cCZ35URO'],
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(settings.BASE_DIR / "db.sqlite3", "rb")
    }
    r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart", headers=headers, files=files)
    print(r.text)
    return 'Uploaded to Drive'
