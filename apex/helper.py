from .models import *
import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# this notification alert system
class channel_alert:
    def notification_alert(subject,text,date,stock_count):
        channel_layer = get_channel_layer()
        notification_objs = Messages.objects.filter(seen__exact = 'False').count()+1
        data = {
            'count': notification_objs,
            'Subject': subject,
            'text': text,
            'date':date,
            'stock_count': stock_count,
        }
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group' , {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )

############################################################

class alertmessages:
    def essentialAlert(typee,quantityy,stock_count):
        if typee == 'Belt' or 'Cylinder' or 'Fevil' or 'Cutter':
            if quantityy <= 20:        
                ms = Messages.objects.create()
                ms.subject = 'Essential Stock Alert'
                ms.text = 'Essential Item ' + typee + ' is low please make new stock'
                ms.seen = 'False'
                ms.stock_count = stock_count
                ms.date = str(datetime.date.today())
                channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
                ms.save()
        elif typee == 'Cutting Oil':
            if quantityy <= 35:        
                ms = Messages.objects.create()
                ms.subject = 'Essential Stock Alert'
                ms.text = 'Essential Item ' + typee + ' is low please make new stock'
                ms.date = str(datetime.date.today())
                ms.stock_count = stock_count
                ms.seen = 'False'
                channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
                ms.save()
        elif typee == 'Polish Wheel' or 'Conjuction Rod':
            if quantityy <= 2:        
                ms = Messages.objects.create()
                ms.subject = 'Essential Stock Alert'
                ms.text = 'Essential Item ' + typee + ' is low please make new stock'
                ms.date = str(datetime.date.today())
                ms.stock_count = stock_count
                ms.seen = 'False'
                channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
                ms.save()
        elif typee == 'Matt Wheel' or 'Buff':
            if quantityy <= 10:        
                ms = Messages.objects.create()
                ms.subject = 'Essential Stock Alert'
                ms.text = 'Essential Item ' + typee + ' is low please make new stock'
                ms.date = str(datetime.date.today())
                ms.stock_count = stock_count
                ms.seen = 'False'
                channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
                ms.save()
        elif typee == 'Plastic Roll' or 'Powder Box':
            if quantityy <= 1:        
                ms = Messages.objects.create()
                ms.subject = 'Essential Stock Alert'
                ms.text = 'Essential Item ' + typee + ' is low please make new stock'
                ms.date = str(datetime.date.today())
                ms.stock_count = stock_count
                ms.seen = 'False'
                channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
                ms.save()
        elif typee == 'Big Carton':
            if quantityy <= 100:        
                ms = Messages.objects.create()
                ms.subject = 'Essential Stock Alert' 
                ms.text = 'Essential Item ' + typee + ' is low please make new stock'
                ms.date = str(datetime.date.today())
                ms.stock_count = stock_count
                ms.seen = 'False'
                channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
                ms.save()
        elif typee == 'Small Plastic':
            if quantityy <= 5:        
                ms = Messages.objects.create()
                ms.subject = 'Essential Stock Alert'
                ms.text = 'Essential Item ' + typee + ' is low please make new stock'
                ms.date = str(datetime.date.today())
                ms.stock_count = stock_count
                ms.seen = 'False'
                channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
                ms.save()

    def rawMaterialAlert(rmm,stock_count):
        if stock_count <= 1500:
            ms = Messages.objects.create()
            ms.subject = 'Raw Material Alert'
            ms.text = 'Coil stock is Low get New Stock'
            ms.date = str(datetime.date.today())
            ms.stock_count = rmm
            ms.seen = 'False'
            channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
            ms.save()
        else:
            pass
    
    # if any material stock law and send notification by employee this function called
    def empty(subject,text,stock_count):
        ms = Messages.objects.create()
        ms.subject = subject
        ms.text = text
        ms.date = str(datetime.date.today())
        ms.stock_count = stock_count
        ms.seen = 'False'
        channel_alert.notification_alert(subject=ms.subject,text=ms.text,stock_count=ms.stock_count,date=ms.date)
        ms.save()

############################################################

class logsave():
    def logg(regid,tbid,operation,tname):
        log = LogTable.objects.create()
        use = User.objects.get(id=regid)
        log.register_id = str(regid)
        log.Username = str(use.username)
        log.CRUDoperation = operation
        log.Table_name = tname
        log.Table_id = str(tbid)
        log.Log_Date = str(datetime.date.today())
        log.save()

############################################################

class scrapsave:
    def scrap_rm(id,weight):
        s = Scrape.objects.create()
        s.S_Type = 'Raw Material'
        s.t_id = id
        s.s_weight = weight
        s.S_date = str(datetime.date.today())
        s.save()

    def scrap_fm(id,weight):
        s = Scrape.objects.create()
        s.S_Type = 'Finish Material'
        s.t_id = id
        s.s_weight = weight
        s.S_date = str(datetime.date.today())
        s.save()

############################################################

class extracting_data_for_graph:
    def dictionary(dic,key,value):
        type = []
        quantity = []
        
        for i in dic:
            type.append(i[key])
            quantity.append(i[value])
        res = {key: [] for key in type}
        for key, val in zip(type, quantity):
            res[key].append(int(val))
        keys = []
        values = []
        for i in res.values():
            values.append(sum(i))
        for i in res.keys():
            keys.append(i)
        res2 = {key: 0 for key in keys}
        for key, val in zip(keys, values):
            res2[key] = val
            
        return res2

    def dict_for_raw(dic,key,value):
        type = []
        quantity = []
        
        for i in dic:
            type.append(str(i[key])[8:])
            quantity.append(i[value])
        res = {key: [] for key in type}
        for key, val in zip(type, quantity):
            res[key].append(int(val))
        keys = []
        values = []
        for i in res.values():
            values.append(sum(i))
        for i in res.keys():
            keys.append(i)
        res2 = {key: 0 for key in keys}
        for key, val in zip(keys, values):
            res2[key] = val
            
        return res2


    def dict_for_fm(dic,key,value):
        type = []
        quantity = []
        
        for i in dic:
            type.append(str(i[key])[5:7])
            quantity.append(i[value])
        res = {key: [] for key in type}
        for key, val in zip(type, quantity):
            res[key].append(int(val))
        keys = []
        values = []
        for i in res.values():
            values.append(sum(i))
        for i in res.keys():
            keys.append(i)
        res2 = {key: 0 for key in keys}
        for key, val in zip(keys, values):
            res2[key] = val
            
        return res2

############################################################

def check_for_null_values(d):
    try:
        total = int(list(d)[-1]) +1
        for i in range(1,total):
                if str(i) not in d:
                    d[i]=0
    except:
        pass

############################################################

# That is for set active and inactive time
def SetTimer(register):
    rg = register # for get all registered object
    user_list = rg.values()

    time = Timmer.objects.filter().last()
    a_time = str(time.active_time) # the 'a' variable defines activeTime
    d_time = str(time.inactive_time) # the 'd' variable defines inActiveTime

    a_hour = int(a_time[0:2])
    a_min = a_time.replace(":",'')[2::]

    d_hour = int(d_time[0:2])
    d_min = d_time.replace(":","")[2::]

    my_time = str(datetime.datetime.now())[10:16].replace(":",'')
    hour = int(my_time[0:2])
    min = my_time[2::]

    a_t = int(str(a_hour)+str(a_min))
    d_t = int(str(d_hour)+str(d_min))
    t = int(str(hour)+str(min))
    
    if t == a_t:
        for i in user_list:
            user_id = i['user_id']
            get_user = Register.objects.get(user_id=user_id)
            get_user.userRole = 'Active'
            get_user.save()
    elif t == d_t:
        for i in user_list:
            user_name = i['UserName']
            status = i['userRole']
            user_id = i['user_id']
            get_user = Register.objects.get(user_id=user_id)
            if user_name == 'Harish':
                get_user.userRole = 'Active'
            else:
                get_user.userRole = 'In-Active'
            get_user.save()
    return "Succed!!!!!!"
    