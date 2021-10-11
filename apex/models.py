import channels
# from django.test import TestCase

# Create your tests here.
from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your models here.

class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    First_Name = models.CharField(max_length=40,null=True,blank=True)
    Last_Name = models.CharField(max_length=40,null=True,blank=True)
    UserName = models.CharField(max_length=40,null=True,blank=True)
    status = models.CharField(max_length=40,null=True,blank=True)
    userRole = models.CharField(max_length=40,null=True,blank=True)
    delete_access = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        return str(self.UserName)


    @staticmethod
    def give_noti_detail(noti_id):
        us = User.objects.get(username = noti_id)
        instance = Register.objects.filter(user = us).first()
        data = {}
        data['delete_access'] = instance.delete_access
        data['userRole'] = instance.userRole
        return data


class rawMaterial(models.Model):
    register = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Vendor = models.CharField(max_length=40,blank=True,null=True)
    RM_Date = models.DateField(blank=True,null=True)
    RM_Thickness = models.CharField(max_length=40,blank=True,null=True)
    RM_Size = models.CharField(max_length=40,blank=True,null=True)
    RM_Grade = models.CharField(max_length=40,blank=True,null=True)
    RM_coilWeight = models.CharField(max_length=40,blank=True,null=True)
    RM_currentCoilWeight = models.CharField(max_length=40,blank=True,null=True)
    RM_scrapWeight = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        return str(self.pk)


class FMstock(models.Model):
    FM_Date = models.DateField(null=True,blank=True)
    register = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    coilUID = models.ForeignKey(rawMaterial,on_delete = models.CASCADE,null=True,blank=True)
    Size = models.CharField(max_length=40,blank=True,null=True)
    Grade = models.CharField(max_length=40,blank=True,null=True)
    coilWeight = models.CharField(max_length=40,blank=True,null=True)
    materialType = models.CharField(max_length=40,null=True,blank=True)#dropdown
    FM_Thickness = models.CharField(max_length=40,null=True,blank=True)
    FM_Size = models.CharField(max_length=40,null=True,blank=True)
    FM_Weight = models.CharField(max_length=40,null=True,blank=True)
    FM_Quantity = models.CharField(max_length=40,null=True,blank=True)
    FM_scrapWeight = models.CharField(max_length=40,null=True,blank=True)
    UF_Thickness = models.CharField(max_length=40,null=True,blank=True)
    UF_Size = models.CharField(max_length=40,null=True,blank=True)
    UF_Weight = models.CharField(max_length=40,null=True,blank=True)
    UF_Quantity = models.CharField(max_length=40,null=True,blank=True)


    def __str__(self):
        return str(self.pk)
        
class UFMstock(models.Model):
    register = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    FMid = models.ForeignKey(FMstock,on_delete = models.CASCADE,null=True,blank=True)
    UFM_type = models.CharField(max_length=40,null=True,blank=True)
    UFM_date = models.DateField(blank=True,null=True)
    UFM_Weight = models.CharField(max_length=40,null=True,blank=True)
    UFM_Quantity = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        return str(self.pk)         

class Sale(models.Model):
    register = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Sale_Type = models.CharField(max_length=40,null=True,blank=True)
    UFcoilID = models.ForeignKey(UFMstock,on_delete = models.CASCADE,null=True,blank=True)
    FMcoilUID = models.ForeignKey(FMstock,on_delete = models.CASCADE,null=True,blank=True)
    Sale_date = models.DateField(blank=True,null=True)
    Sale_Weight = models.CharField(max_length=40,null=True,blank=True)
    Sale_Quantity = models.CharField(max_length=40,null=True,blank=True)
    Stock = models.CharField(max_length=40,null=True,blank=True)
    To = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        return str(self.id)

class Scrape(models.Model):
    S_Type = models.CharField(max_length=40,null=True,blank=True)
    t_id = models.CharField(max_length=40,null=True,blank=True)
    s_weight = models.CharField(max_length=40,null=True,blank=True)
    S_date = models.DateField(blank=True,null=True)

class essentialitemStock(models.Model):
    register = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Type = models.CharField(max_length=400,null=True,blank=True)
    ES_Date = models.DateField(null=True,blank=True)
    ES_Size = models.CharField(max_length=400,null=True,blank=True)
    ES_Quantity = models.CharField(max_length=400,null=True,blank=True)

    def __str__(self):
        return str(self.pk)

class EssentialItemUsePerDay(models.Model):
    register = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    EPD_Type = models.CharField(max_length=40,null=True,blank=True)
    EPD_Size = models.CharField(max_length=40,null=True,blank=True)
    EPD_UID = models.ForeignKey(essentialitemStock,on_delete = models.CASCADE,null=True)
    EPD_Date = models.DateField(null=True,blank=True)
    EPD_Quantity = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        return str(self.pk)


class LogTable(models.Model):
    register_id = models.CharField(max_length=40,null=True,blank=True)
    Username = models.CharField(max_length=40,null=True,blank=True)
    CRUDoperation = models.CharField(max_length=40,null=True,blank=True)
    Table_name = models.CharField(max_length=40,null=True,blank=True)
    Table_id = models.CharField(max_length=40,null=True,blank=True)
    Log_Date = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return str(self.Table_name)

class Notification(models.Model):
    register = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    text = models.CharField(max_length=40,null=True,blank=True)
    # date = models.DateField(max_length=40,null=True,blank=True)


class Messages(models.Model):
    subject = models.CharField(max_length=400,null=True,blank=True)
    text = models.CharField(max_length=400,null=True,blank=True)
    date = models.CharField(max_length=400,null=True,blank=True)
    stock_count = models.CharField(max_length=400,null=True,blank=True)
    seen = models.CharField(max_length=400,null=True,blank=True)
    def __str__(self):
        return str(self.subject)

    # def save(self, *args,**kwargs):
    #     print('save method called of messages')
    #     channel_layer = get_channel_layer()
    #     notification_objs = Messages.objects.filter().count()
    #     data = {
    #         'count': notification_objs,
    #         'Subject': self.subject,
    #         'text': self.text,
    #         'date':self.date,
    #         'stock_count': self.stock_count,
    #     }
    #     print(f'{data} ********************************************')
    #     async_to_sync(channel_layer.group_send)(
    #         'test_consumer_group' , {
    #             'type': 'send_notification',
    #             'value': json.dumps(data)

    #         }
    #     )
    #     super(Messages, self).save(*args, **kwargs)
# we'll create a message model where all the messages will be stored 
# whenever raw meterial count is 2 send notification
# we need if loop to check the count 
# if count is 2 or less then 2 message model will be called and message will be saved
# then that saved message will be shown to admin via channels

class Deleted_tables(models.Model):
    table_name = models.CharField(max_length=40,null=True,blank=True)
    material_id = models.CharField(max_length=40,null=True,blank=True)
    quantity = models.CharField(max_length=40,null=True,blank=True)
    size = models.CharField(max_length=40,null=True,blank=True)
    type = models.CharField(max_length=40,null=True,blank=True)
    weight = models.CharField(max_length=40,null=True,blank=True)
    date = models.CharField(max_length=40,null=True,blank=True)

class Timmer(models.Model):
    active_time = models.CharField(max_length=40,null=True,blank=True)
    inactive_time = models.CharField(max_length=40,null=True,blank=True)

