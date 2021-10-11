
from re import L
from datetime import date
import django_filters
from django import forms
from django_filters import DateFilter
from django_filters.filters import CharFilter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import *

# this is for disable all future date in frontend
today = date.today()

# this is our raw material date filter
class RMFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='RM_Date', label='', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date', 'max':f'{today}', 'placeholder': 'Start Date', 'class': 'mr-2 id_start_date'}))
    end_date = DateFilter(field_name='RM_Date', label='', lookup_expr='lte' , widget=forms.DateInput(attrs={'type': 'date', 'max':f'{today}', 'placeholder': 'End Date', 'class': 'mr-2 id_end_date'}))

    class Meta:
        model = rawMaterial
        fields = '__all__'
        exclude = ['register', 'RM_coilWeight', 'RM_scrapWeight',
                'RM_Thickness', 'RM_Size', 'RM_Grade', 'RM_Date', 'receiver',"Vendor", "RM_currentCoilWeight"]


class LogTableFilter(django_filters.FilterSet):
    username = CharFilter(field_name='Username', label='', lookup_expr='icontains', widget=forms.TextInput(attrs={'type': 'text', 'style': 'max-width: 280px;', 'placeholder': 'Username'}))
    crud = CharFilter(field_name='CRUDoperation', label='', lookup_expr='icontains', widget=forms.TextInput(attrs={'type': 'text', 'style': 'max-width: 280px;', 'placeholder': 'Operation'}))
    date = DateFilter(field_name='Log_Date', label='', widget=forms.DateInput(attrs={'type': 'date', 'max':f'{today}', 'placeholder': 'Date'}))

    class Meta:
        model = LogTable
        fields = '__all__'
        exclude = ['Username', 'CRUDoperation', 'Log_Date',
                'Table_name', 'register_id', 'Table_id', ]

# this is our finished material date filter
class FMfilter(django_filters.FilterSet):
    # size = CharFilter(field_name='FM_Size', label='', lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Size'}))
    # mtype = CharFilter(field_name='materialType', label='', lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Type'}))
    # date = DateFilter(field_name='FM_Date', label='', widget=forms.DateInput(
    #     attrs={'type': 'date', 'placeholder': 'Date'}))

    start_date = DateFilter(field_name='FM_Date', label='', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date', 'max':f'{today}','placeholder': 'Start Date', 'class': 'mr-2'}))

    end_date = DateFilter(field_name='FM_Date', label='', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date', 'max':f'{today}','placeholder': 'End Date', 'class': 'mr-2'}))


    class Meta:
        model = FMstock
        fields = '__all__'
        exclude = ['FM_Date', 'register', 'coilUID', 'Size', 'Grade', 'coilWeight', 'materialType', 'FM_Thickness', 'FM_Size',
                'FM_Weight', 'FM_Quantity', 'FM_scrapWeight', 'UF_Thickness', 'UF_Size', 'UF_Weight', 'UF_Quantity']

# this is essential material data filter
class EMfilter(django_filters.FilterSet):
    # estype = CharFilter(field_name='Type', label='', lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Type'}))
    # size = CharFilter(field_name='ES_Size', label='', lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Size'}))
    # date = DateFilter(field_name='ES_Date', label='', widget=forms.DateInput(
    #     attrs={'type': 'date', 'placeholder': 'Date'}))

    start_date = DateFilter(field_name='ES_Date', label='', lookup_expr='gte',widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'Start Date', 'class': 'mr-2'}))

    end_date = DateFilter(field_name='ES_Date', label='', lookup_expr='lte',widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'End Date', 'class': 'mr-2'}))

    class Meta:
        model = essentialitemStock
        fields = '__all__'
        exclude = ['register', 'Type', 'ES_Quantity', 'ES_Size', 'ES_Date']

# this  is unfinished material date fileter
class UFMFilter(django_filters.FilterSet):
    # date = DateFilter(field_name='UFM_date', label='', widget=forms.DateInput(
    #     attrs={'type': 'date', 'placeholder': 'Date'}))
    # weight = CharFilter(field_name='UFM_Weight', label='', lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Weight'}))

    start_date = DateFilter(field_name='UFM_date', label='', lookup_expr='gte',widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'Start Date', 'class': 'mr-2'}))

    end_date = DateFilter(field_name='UFM_date', label='', lookup_expr='lte',widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'End Date', 'class': 'mr-2'}))

    class Meta:
        model = UFMstock
        fields = '__all__'
        exclude = ['register', 'UFM_Quantity', 'FMid',
                    'UFM_date', 'UFM_Weight', 'UFM_type']


class scrapeFilter(django_filters.FilterSet):
    # date = DateFilter(field_name='S_date', label='', widget=forms.DateInput(
    #     attrs={'type': 'date', 'placeholder': 'Date'}))
    # type = CharFilter(field_name='S_Type', label='', lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Type'}))
    # weight = CharFilter(field_name='s_weight', label='', lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Weight'}))

    start_date = DateFilter(field_name='S_Date', label='', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'Start Date', 'class': 'mr-2'}))

    end_date = DateFilter(field_name='S_Date', label='', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'End Date', 'class': 'mr-2'}))

    class Meta:
        model = Scrape
        fields = '__all__'
        exclude = ['S_Type', 't_id', 'S_date', 's_weight']


class fsaleFilter(django_filters.FilterSet):
    # fid = CharFilter(field_name='FMcoilUID', label='', widget=forms.TextInput(attrs={
    #                  'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'FM ID'}))
    # date = DateFilter(field_name='Sale_date', label='', widget=forms.DateInput(
    #     attrs={'type': 'date', 'placeholder': 'Date'}))

    start_date = DateFilter(field_name='Sale_date', label='', lookup_expr='gte',
                            widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'Start Date', 'class': 'mr-2'}))

    end_date = DateFilter(field_name='Sale_date', label='', lookup_expr='lte',
                        widget=forms.DateInput(attrs={'type': 'date', 'max':f'{today}','placeholder': 'End Date', 'class': 'mr-2'}))

    class Meta:
        model = Sale
        fields = '__all__'
        exclude = ['FMcoilUID', 'Sale_date', 'register', 'Sale_Type',
                    'Sale_Weight', 'UFcoilID', 'Sale_Weight', 'Sale_Quantity', 'Stock', 'supplier']


class ufsaleFilter(django_filters.FilterSet):
    # ufid = CharFilter(field_name='UFcoilID', label='', widget=forms.TextInput(attrs={
    #                   'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'UFM ID'}))
    # date = DateFilter(field_name='Sale_date', label='', widget=forms.DateInput(
    #     attrs={'type': 'date', 'placeholder': 'Date'}))

    start_date = DateFilter(field_name='Sale_date', label='', lookup_expr='gte',
                            widget=forms.DateInput(attrs={'type': 'date', 'max':f'{today}','placeholder': 'Start Date', 'class': 'mr-2'}))

    end_date = DateFilter(field_name='Sale_date', label='', lookup_expr='lte',
                        widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'End Date', 'class': 'mr-2'}))

    class Meta:
        model = Sale
        fields = '__all__'
        exclude = ['FMcoilUID', 'Sale_date', 'register', 'Sale_Type',
                    'Sale_Weight', 'UFcoilID', 'Sale_Weight', 'Sale_Quantity', 'Stock', 'supplier']


class usageFilter(django_filters.FilterSet):
    # etype = CharFilter(field_name='EPD_Type', label='', lookup_expr='icontains', widget=forms.TextInput(
    #     attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Material Type'}))
    # date = DateFilter(field_name='EPD_Date', label='', widget=forms.DateInput(
    #     attrs={'type': 'date', 'placeholder': 'Date'}))

    start_date = DateFilter(field_name='EPD_Date', label='', lookup_expr='gte',
                            widget=forms.DateInput(attrs={'type': 'date','max':f'{today}', 'placeholder': 'Start Date', 'class': 'mr-2'}))

    end_date = DateFilter(field_name='EPD_Date', label='', lookup_expr='lte',
                            widget=forms.DateInput(attrs={'type': 'date', 'max':f'{today}','placeholder': 'End Date', 'class': 'mr-2'}))

    class Meta:
        model = EssentialItemUsePerDay
        fields = '__all__'
        exclude = ['EPD_Type', 'EPD_Date', 'register',
                    'EPD_Size', 'EPD_UID', 'EPD_Quantity']


class empFilter(django_filters.FilterSet):
    name = CharFilter(field_name='UserName', label='', lookup_expr='icontains', widget=forms.TextInput(
        attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Username'}))
    userRole = CharFilter(field_name='userRole', label='', lookup_expr='icontains', widget=forms.TextInput(
        attrs={'type': 'text', 'style': 'max-width: 120px; min-width: 100px;', 'placeholder': 'User Role'}))
    # role = CharFilter(field_name='userRole', label='', lookup_expr='icontains',widget=forms.TextInput(attrs={'type': 'text','style':'max-width: 120px; min-width: 100px;','placeholder': 'User Role'}))
    status = CharFilter(field_name='status', label='', lookup_expr='icontains', widget=forms.TextInput(
        attrs={'type': 'text', 'style': 'max-width: 120px; min-width: 100px;', 'placeholder': 'User Status'}))

    class Meta:
        model = Register
        fields = '__all__'
        exclude = ['UserName', 'user', 'First_Name', 'Last_Name']


class deletedFilter(django_filters.FilterSet):
    delid = CharFilter(field_name='material_id', label='', lookup_expr='icontains', widget=forms.TextInput(
        attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Material ID'}))
    date = DateFilter(field_name='date', label='', widget=forms.DateInput(
        attrs={'type': 'date','max':f'{today}', 'placeholder': 'Date'}))
    deltype = CharFilter(field_name='type', label='', lookup_expr='icontains', widget=forms.TextInput(
        attrs={'type': 'text', 'style': 'max-width: auto; min-width: 100px;', 'placeholder': 'Type'}))

    class Meta:
        model = Deleted_tables
        fields = '__all__'
        exclude = ['material_id', 'type', 'date',
                'table_name', 'quantity', 'size', 'weight']
