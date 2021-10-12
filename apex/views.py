from datetime import date
# import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .decoraters import *
from .filters import *
from .task import *
from .helper import *
from django.contrib import messages
# Create your views here.

# this is for disable all future date in frontend and variable pass in context
date = date.today()
todayDate = date.strftime('%Y-%m-%d')

#Admin Dashboard View 
@login_required(login_url='login') # decorator for required login
@allowed_users(allowed_roles=['admin'])# allowed user decorator only admin can access this view
def Admin_Dashboard(request):
    header = 'Overview'
    today = date.today()
    start_date = datetime.datetime.now() + datetime.timedelta(-6)
    
    # filtering data for dashboard page grahs
    essential_items = essentialitemStock.objects.filter(ES_Date__year=today.year, ES_Date__month=today.month, ES_Date__range=[start_date, today]).values() 
    essential_usage = EssentialItemUsePerDay.objects.filter(EPD_Date__year=today.year, EPD_Date__month=today.month, EPD_Date__range=[start_date, today]).values() 
    sale = Sale.objects.filter(Sale_date__year=today.year).values()
    raw_material = rawMaterial.objects.filter(RM_Date__year=today.year, RM_Date__month=today.month).values()
    finished_material = FMstock.objects.filter(FM_Date__year=today.year).values()
    
    # extracting data from filtered accordingly in dictionary formate
    raw_material_weight = extracting_data_for_graph.dict_for_raw(dic=raw_material, key='RM_Date', value='RM_coilWeight')
    check_for_null_values(d=raw_material_weight)
    raw_material_scrap = extracting_data_for_graph.dict_for_raw(dic=raw_material, key='RM_Date', value='RM_scrapWeight')
    check_for_null_values(d=raw_material_scrap)

    finished_material_weight = extracting_data_for_graph.dict_for_raw(dic=finished_material, key='FM_Date', value='FM_Weight')
    check_for_null_values(d=finished_material_weight)
    finished_material_scrap = extracting_data_for_graph.dict_for_raw(dic=finished_material, key='FM_Date', value='FM_scrapWeight')
    check_for_null_values(d=finished_material_scrap)

    finished_material_quantity = extracting_data_for_graph.dict_for_fm(dic=finished_material, key='FM_Date', value='FM_Quantity')

    essential_stock = extracting_data_for_graph.dictionary(dic=essential_items, key='Type', value='ES_Quantity')
    essential_use = extracting_data_for_graph.dictionary(dic=essential_usage, key='EPD_Type', value='EPD_Quantity')

    sale_items = extracting_data_for_graph.dict_for_fm(dic=sale, key='Sale_date', value='Sale_Quantity')

    # dumping all dictionaries in json
    raw_material_weight_dict = json.dumps(raw_material_weight)
    raw_material_scrap_dict = json.dumps(raw_material_scrap)
    finished_material_weight_dict = json.dumps(finished_material_weight)
    finished_material_scrap_dict = json.dumps(finished_material_scrap)
    finished_material_quantity_dict = json.dumps(finished_material_quantity)
    essential_use_dict = json.dumps(essential_use)
    essential_dict = json.dumps(essential_stock)
    sale_dict = json.dumps(sale_items)

    #loading dumped data 
    raw_material_weight_graph = json.loads(raw_material_weight_dict)
    raw_material_scrap_graph = json.loads(raw_material_scrap_dict)
    finished_material_weight_graph = json.loads(finished_material_weight_dict)
    finished_material_scrap_graph = json.loads(finished_material_scrap_dict)
    finished_material_quantity_graph = json.loads(finished_material_quantity_dict)
    essential_use_graph = json.loads(essential_use_dict)
    essential_items_graph = json.loads(essential_dict)
    sale_graph = json.loads(sale_dict)

    # rendering all message in notfication modal in reverse order so the new message is always on top
    all_messages = Messages.objects.all().order_by("-id")
    # rendering last 5 messages for dropdown notification in reverse order
    filter_message = Messages.objects.filter().order_by('-id')[:5]
    # rendering count of all messages
    message_count = str(Messages.objects.filter(seen__exact='False').count())
    #rendering scrap material table
    scrap_items = Scrape.objects.all()

    return render(request, 'apex/overview.html', {'header': header, 'ms': filter_message, 'ms_count': message_count, 'all_ms': all_messages,
                                                'scrap_t': scrap_items, 'raw_material_weight_graph': raw_material_weight_graph, 'raw_material_scrap_graph': raw_material_scrap_graph, 'finished_material_weight_graph': finished_material_weight_graph,
                                                'finished_material_scrap_graph': finished_material_scrap_graph, 'finished_material_quantity_graph': finished_material_quantity_graph, 'sale_graph': sale_graph, 'essential_items_graph': essential_items_graph, 'essential_use_graph': essential_use_graph})

########################################################################

# user account page view
@login_required(login_url='login') # decorator for required login
def Account(request):
    header = 'Account'
    # rendering time on emplayee account tab
    time = Timmer.objects.filter().last()
    a_time = str(time.active_time)
    d_time = str(time.inactive_time)
    # rendering all message in notfication modal in reverse order so the new message is always on top
    all_messages = Messages.objects.all().order_by("-id")
    # rendering last 5 messages for dropdown notification in reverse order
    message_filter = Messages.objects.filter().order_by('-id')[:5]
    # rendering count of all messages
    message_count = str(Messages.objects.filter(seen__exact='False').count())
    #geting user data for my account tab
    user_account = Register.objects.get(user__id=request.user.id)
    #rendering user data for employee account tab
    all_user = Register.objects.all()
    #rendering deleted tables data on deleted tables tab
    delete_tables = Deleted_tables.objects.all()
    
    context = {}
    # passing data in context
    context['room_code'] = user_account.user.username
    context['data'] = user_account
    context['all_user'] = all_user
    context['header'] = header
    context['ms_count'] = message_count
    context['ms'] = message_filter
    context['all_ms'] = all_messages
    context['delete_tables'] = delete_tables
    context['a_time'] = a_time
    context['d_time'] = d_time

    return render(request, 'apex/account.html', context)

########################################################################

# Raw material page view
@login_required(login_url='login') # decorator for required login
def User_Raw_Material(request):
    header = 'Raw Material Stock'

    # rendering all message in notfication modal in reverse order so the new message is always on top
    all_messages = Messages.objects.all().order_by("-id")
    # rendering last 5 messages for dropdown notification in reverse order
    filter_message = Messages.objects.filter().order_by('-id')[:5]
    # rendering count of all messages
    message_count = str(Messages.objects.filter(seen__exact='False').count())
    # rendering raw material data in table
    all_raw_materials = rawMaterial.objects.all()
    #rendering log table for raw material data
    log = LogTable.objects.filter(Table_name__exact='Raw Material')
    # date filters 
    raw_material_filter = RMFilter(request.GET, queryset=all_raw_materials)
    raw_material_data = raw_material_filter.qs
    # getting users to to check if their access provided by admin
    user_id = User.objects.get(id=request.user.id)
    register = Register.objects.get(user=user_id)
    # geting start and end date from date filters

    try:
        startDate = request.GET['start_date']
        endDate = request.GET['end_date']
    except:
        startDate = None
        endDate = None
#start if else
    #filtering raw table in graph
    if startDate and endDate != None:
        # rendering raw data from date filters to graph
        raw_material_data = rawMaterial.objects.filter(RM_Date__gte=startDate, RM_Date__lte=endDate).values()
        # extracting grade and coilweight from filtered data
        raw_material_coilweight = extracting_data_for_graph.dictionary(dic=raw_material_data, key='RM_Grade', value='RM_coilWeight')
        # dumping extracted data
        raw_material_coilweight_dict = json.dumps(raw_material_coilweight)
        # laoding data
        raw_material_coilweight_graph = json.loads(raw_material_coilweight_dict)
    else:
        # rending all raw data to graph
        raw_material_data = rawMaterial.objects.values()
        # extracting grade and coilweight from filtered data
        raw_material_coilweight = extracting_data_for_graph.dictionary(dic=raw_material_data, key='RM_Grade', value='RM_coilWeight')
        # dumping extracted data    
        raw_material_coilweight_dict = json.dumps(raw_material_coilweight)
        # laoding data
        raw_material_coilweight_graph = json.loads(raw_material_coilweight_dict)
#end if else

    context = {'raw_material_data': raw_material_data, 'date':todayDate,'log': log, 'raw_material_filter': raw_material_filter,  'header': header, 'ms': filter_message, 'ms_count': message_count, 'all_ms': all_messages, 'raw_material_coilweight_graph': raw_material_coilweight_graph, 'delete_access': str(register.delete_access),
        'role': str(register.userRole),'username':'saif','room_code':'admin'}
    return render(request, 'apex/raw_material.html', context)


########################################################################

@login_required(login_url='login')# decorator for required login
def User_UnFinished_Material(request):
    header = 'Un-Finished Material Stock'
    # rendering all message in notfication modal in reverse order so the new message is always on top
    all_messages = Messages.objects.all().order_by("-id")
    # rendering last 5 messages for dropdown notification in reverse order
    filter_message = Messages.objects.filter().order_by('-id')[:5]
    # rendering count of all messages
    message_count = str(Messages.objects.filter(seen__exact='False').count())
    # rendering data in ufm table
    all_ufm_data = UFMstock.objects.all()
    # rendering data in fm table
    all_fm_stock = FMstock.objects.all()
    # rendering sales data
    sale_filter = Sale.objects.filter(Stock__exact='Un-Finished Material Stock')
    # rendering logtable
    log = LogTable.objects.filter(Table_name__exact='Un-Finished Material Stock')
    # filters
    ufm_filter = UFMFilter(request.GET, queryset=all_ufm_data)
    Ufm_sale = ufsaleFilter(request.GET, queryset=sale_filter)
    __ufm_data = ufm_filter.qs
    __Ufm_sale = Ufm_sale.qs
    # getting users to to check if their access provided by admin
    user_id = User.objects.get(id=request.user.id)
    register = Register.objects.get(user=user_id)
    # geting start and end date from date filters
    try:
        startDate = request.GET['start_date']
        endDate = request.GET['end_date']
    except:
        startDate = None
        endDate = None
#start if else
    if startDate and endDate != None:
        # rendering ufm data from date filters to graph
        ufm_data = UFMstock.objects.filter(UFM_date__gte=startDate, UFM_date__lte=endDate).values()
        sale_data = Sale.objects.filter(Stock__exact='Un-Finished Material Stock', Sale_date__gte=startDate, Sale_date__lte=endDate).values()
        # extracting grade and ufm type from filtered data
        ufm_quantity = extracting_data_for_graph.dictionary(dic=ufm_data, key='UFM_type', value='UFM_Quantity')
        # extracting grade and sale type from filtered data
        sale_quantity = extracting_data_for_graph.dictionary(dic=sale_data, key='Sale_Type', value='Sale_Quantity')
        # dumping data in json
        ufm_quantity_dict = json.dumps(ufm_quantity)
        sale_dict = json.dumps(sale_quantity)
        #loading in json
        ufm_quantity_graph = json.loads(ufm_quantity_dict)
        sale_quantity_graph = json.loads(sale_dict)
    else:
        # rendering ufm data in graph
        ufm_data = UFMstock.objects.values()
        sale_data = Sale.objects.filter(Stock__exact='Un-Finished Material Stock').values()
        # extracting grade and ufm type from filtered data
        ufm_quantity = extracting_data_for_graph.dictionary(dic=ufm_data, key='UFM_type', value='UFM_Quantity')
        # extracting grade and sale type from filtered data
        sale_quantity = extracting_data_for_graph.dictionary(dic=sale_data, key='Sale_Type', value='Sale_Quantity')
        ufm_quantity_dict = json.dumps(ufm_quantity)
        sale_dict = json.dumps(sale_quantity)
        ufm_quantity_graph = json.loads(ufm_quantity_dict)
        sale_quantity_graph = json.loads(sale_dict)
#end if else
    context = {'ufm_data': __ufm_data, 'date':todayDate, 'log': log, 'ufm_sale_data': __Ufm_sale, 'header': header, 'ms_count': message_count, 'ms': filter_message, 'data3': all_fm_stock, 'all_ms': all_messages,
        'UFfilter': ufm_filter, 'Ufsale': Ufm_sale, 'ufm_quantity_graph': ufm_quantity_graph, 'sale_quantity_graph': sale_quantity_graph, 'delete_access': str(register.delete_access),
        'role': str(register.userRole)}
    return render(request, 'apex/unfinished_material.html', context)

########################################################################

#Finished Material View
@login_required(login_url='login')
def User_Finished_Material(request):
    header = 'Finished Material Stock'
    # rendering all message in notfication modal in reverse order so the new message is always on top
    all_messages = Messages.objects.all().order_by("-id")
    # rendering last 5 messages for dropdown notification in reverse order
    filter_massage = Messages.objects.filter().order_by('-id')[:5]
    # rendering count of all messages
    message_count = str(Messages.objects.filter(seen__exact='False').count())
    # rendering data in fm table
    all_fm_data = FMstock.objects.all()
    #rendering rawMaterial data in table
    all_raw_material = list(rawMaterial.objects.all())
    #rendering Sale data in table
    sale_filter = Sale.objects.filter(Stock__exact='Finished Material Stock')
    #rendering Logtable 
    log = LogTable.objects.filter(Table_name__exact='Finished Material Stock')
    #filters
    fm_stock_filter = FMfilter(request.GET, queryset=all_fm_data)
    fm_sale = fsaleFilter(request.GET, queryset=sale_filter)
    __fm_sale = fm_sale.qs
    __fm_stock = fm_stock_filter.qs
    __fm_stocks = fm_stock_filter.qs
    # getting users to to check if their access provided by admin
    user_id = User.objects.get(id=request.user.id)
    register = Register.objects.get(user=user_id)
    # geting start and end date from date filters
    try:
        startDate = request.GET['start_date']
        endDate = request.GET['end_date']
    except:
        startDate = None
        endDate = None
#start if else
    if startDate and endDate != None:
        # rendering fm data and sale data from date filters to graph
        fm_data = FMstock.objects.filter(FM_Date__gte=startDate, FM_Date__lte=endDate).values()
        sale_data = Sale.objects.filter(Stock__exact='Finished Material Stock', Sale_date__gte=startDate, Sale_date__lte=endDate).values()
        # extracting quantity and type from filtered data
        fm_quantity = extracting_data_for_graph.dictionary(dic=fm_data, key='materialType', value='FM_Quantity')
        sale_quantity = extracting_data_for_graph.dictionary(dic=sale_data, key='Sale_Type', value='Sale_Quantity')
        # dumping data in json
        fm_quantity_dict = json.dumps(fm_quantity)
        sale_quantity_dict = json.dumps(sale_quantity)
        #loading data in json
        fm_quantity_graph = json.loads(fm_quantity_dict)
        sale_quantity_graph = json.loads(sale_quantity_dict)
    else:
        # rendering fm data and sale data in graph
        fm_data = FMstock.objects.values()
        sale_data = Sale.objects.filter(Stock__exact='Finished Material Stock').values()
        # extracting quantity and type from filtered data
        fm_quantity = extracting_data_for_graph.dictionary(dic=fm_data, key='materialType', value='FM_Quantity')
        sale_quantity = extracting_data_for_graph.dictionary(dic=sale_data, key='Sale_Type', value='Sale_Quantity')
        #dumps data in json
        fm_quantity_dict = json.dumps(fm_quantity)
        sale_quantity_dict = json.dumps(sale_quantity)
        #loads data in json
        fm_quantity_graph = json.loads(fm_quantity_dict)
        sale_quantity_graph = json.loads(sale_quantity_dict)
#end if else

    context = {'fm_stock': __fm_stock,'date':todayDate,'datas': __fm_stocks, 'log': log, 'fm_sale': __fm_sale, 'fmstockfilter': fm_stock_filter, 'header': header, 'all_raw_material': all_raw_material, 'ms_count': message_count, 'ms': filter_massage, 'all_ms': all_messages,  'fmstockfilter': fm_stock_filter,
        'fmsale': fm_sale, 'fm_quantity_graph': fm_quantity_graph, 'sale_quantity_graph': sale_quantity_graph, 'delete_access': str(register.delete_access),
        'role': str(register.userRole)}
    return render(request, 'apex/finished_material.html', context)

########################################################################

# @unautherized_user
# essential material page view
@login_required(login_url='login')
def User_Essential_Material(request):
    header = 'Essential Item Stock'
    # rendering all message in notfication modal in reverse order so the new message is always on top
    all_messages = Messages.objects.all().order_by("-id")
    # rendering last 5 messages for dropdown notification in reverse order
    filter_message = Messages.objects.filter().order_by('-id')[:5]
    # rendering count of all messages
    message_count = str(Messages.objects.filter(seen__exact='False').count())
    # rendering es stock data in table
    all_es_data = essentialitemStock.objects.all()
    # rendering es user per day data in es table
    essential_usage = EssentialItemUsePerDay.objects.all()
    # rendering es log table
    log = LogTable.objects.filter(Table_name__exact='Essential Item Stock')
    # date filters
    essential_filter = EMfilter(request.GET, queryset=all_es_data)
    essential_usage_filter = usageFilter(request.GET, queryset=essential_usage)
    __essential_usage = essential_usage_filter.qs
    __essential = essential_filter.qs
    # getting users to to check if their access provided by admin
    user_id = User.objects.get(id=request.user.id)
    register = Register.objects.get(user=user_id)
    # rendering graphs from filters
    try:
        startDate = request.GET['start_date']
        endDate = request.GET['end_date']
    except:
        startDate = None
        endDate = None
#start if else
    if startDate and endDate != None:
        # rendering data from date filters to graph
        essential = essentialitemStock.objects.filter(ES_Date__gte=startDate, ES_Date__lte=endDate).values()
        #extracting type and its quantity from es table
        essential_data = extracting_data_for_graph.dictionary(dic=essential, key='Type', value='ES_Quantity')
        # dumping in json
        essential_data_dict = json.dumps(essential_data)
        # loading in json
        essential_data_graph = json.loads(essential_data_dict)
    else:
        # rendering total es data in graph 
        essential = essentialitemStock.objects.values()
        essential_data = extracting_data_for_graph.dictionary(dic=essential, key='Type', value='ES_Quantity')
        # dumping json
        essential_data_dict = json.dumps(essential_data)
        #loading json
        essential_data_graph = json.loads(essential_data_dict)
#end if else

    context = {'essential_data': __essential,'date':todayDate, 'log': log, 'essential_usage': __essential_usage, 'header': header, 'ms_count': message_count, 'ms': filter_message, 'all_ms': all_messages,  'emfilter': essential_filter, 'usage': essential_usage_filter, 'essential_data_graph': essential_data_graph, 'd_access': str(register.delete_access),
        'role': str(register.userRole),'room_code':register.user,'delete_access':register.delete_access,'user_role':register.userRole}
    return render(request, 'apex/essential_material.html', context)

########################################################################

#Delete View
@unautherized_user
def delete(request):
    # checks the request Method
    if request.method == 'POST':
        #getting the inputs values
        register_id = request.POST.get('sid')
        user_register = Register.objects.get(pk=register_id)
        #deleting the user 
        user_register.delete()
        # returning in Json if true
        return JsonResponse({'status': 1})
    else:
        # returning in Json if false
        return JsonResponse({'status': 0})
########################################################################

# Notification sending view
def Notifcation_Send(request):

    # checks the request Method
    if request.method == "POST":
        # getting the inputs values
        table_name = request.POST['table_name']
        subject = request.POST['subject']
        operation = request.POST['operation']
        reason = request.POST['reason']
        user = User.objects.get(id=request.user.id)
        rs = Register.objects.get(user=user)
        role = rs.userRole
        # Check the user is active or not
        if role == 'Active':
            text = "{} sent a notifcation for table: {} Subject: {}, Operation: {}, Reason: {}".format(
                user.username, table_name, subject, operation, reason)
            alertmessages.empty(subject='Notification Alert',text=text, stock_count='')
        else:
            text = "{} sent a notifcation for table: {} Subject: {}, Operation: {}, Reason: {}".format(
                user.username, table_name, subject, operation, reason)
            alertmessages.empty(subject='Request Access',text=text, stock_count='')
        # returning in Json 
        return JsonResponse({'status': 'Save'})
    else:
        return JsonResponse({'status': 0})

########################################################################

# this is our login system
@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            register = Register.objects.get(user=user.id)
            status = register.status
            if status == 'Approved':
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'You are not approved')
                return redirect('login')
        else:
            messages.error(request, 'Wrong Credentials')

    return render(request, 'auth/login.html')

########################################################################

# register page function
def userRegister(request):
    return render(request, 'auth/register.html')

########################################################################

# this function get raw data
def get_raw_material_grade(request, *args, **kwargs):
    selected_id = kwargs.get('id')
    rw_grade = list(rawMaterial.objects.filter(id=selected_id).values())
    return JsonResponse({'data': rw_grade})

########################################################################

# this functions saves raw data
@unautherized_user
def Raw_Material_Save(request):
    if request.method == 'GET':
        raw_material = list(rawMaterial.objects.values())
        return JsonResponse({'data': raw_material})

    if request.method == "POST":
        vendor = request.POST['raw_material_vendor']
        raw_material_date = request.POST['raw_material_date']
        raw_material_thickness = request.POST['raw_material_thickness']
        raw_material_size = request.POST['raw_material_size']
        raw_material_grade = request.POST['raw_material_grade']
        raw_material_coil_weight = request.POST['raw_material_coilweight']
        raw_material_scrap_weight = request.POST['raw_material_scrapweight']
        user = User.objects.get(id=request.user.id)
        rawMaterial.objects.create(register=user, RM_Date=raw_material_date, RM_Thickness=raw_material_thickness,  RM_Size=raw_material_size, RM_Grade=raw_material_grade,RM_currentCoilWeight=raw_material_coil_weight, RM_coilWeight=raw_material_coil_weight, RM_scrapWeight=raw_material_scrap_weight,Vendor=vendor)

        raw_material_save = list(rawMaterial.objects.values())
        
        return JsonResponse({'status': 'Save', 'raw_data1': raw_material_save})
    else:
        return JsonResponse({'status': 0})

########################################################################

# this function deletes raw data
@del_access
@unautherized_user
def Raw_Material_Delete(request):
    if request.method == "POST":
        raw_id = request.POST['sid']
        user = User.objects.get(id=request.user.id)
        logsave.logg(regid=user.id, tbid=raw_id, operation='Entry Deleted', tname='Raw Material')
        try:
            raw_material = rawMaterial.objects.get(id=raw_id)
            scrape = Scrape.objects.get(t_id=raw_id)
            raw_material.delete()
            scrape.delete()
        except:
            raw_material = rawMaterial.objects.get(id=raw_id)
            raw_material.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})

########################################################################

# this function saves unfinished material data.
@unautherized_user
def Unfinished_Material_Save(request):
    if request.method == 'POST':
        ufm_date = request.POST['uf_date']
        ufm_id = request.POST['f_id']
        ufm_weight = request.POST['uf_weight']
        ufm_quantity = request.POST['uf_quantity']
        fm_id = FMstock.objects.get(id=ufm_id)
        user = User.objects.get(id=request.user.id)
        unfinished_material = UFMstock(UFM_date=ufm_date, UFM_Weight=ufm_weight, UFM_Quantity=ufm_quantity, register=user, FMid=fm_id)
        unfinished_material.save()

        unfinished_material_value = list(UFMstock.objects.values())
        
        return JsonResponse({'status': 'Save', 'uf_data': unfinished_material_value})
    else:
        return JsonResponse({'Status': 0})

########################################################################

# this function deletes unfinished material data
@del_access
@unautherized_user
def Unfinished_Material_Delete(request):
    if request.method == "POST":
        ufm_id = request.POST['sid']
        user = User.objects.get(id=request.user.id)
        logsave.logg(regid=user.id, tbid=ufm_id, operation='Entry Deleted',
                    tname='Un-Finished Material Stock')
        uf = UFMstock.objects.get(id=ufm_id)
        uf.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})

########################################################################

# this function saves finished material data
@unautherized_user
def Finished_Material_Save(request):
    ''' rm(Raw_material) fm(Finished_material) uf(Unfinished_material) '''

    if request.method == 'POST':
        rm_id = request.POST['raw_id']
        rm_size = request.POST['raw_size']
        date = request.POST['fmat_date']
        rm_grade = request.POST['raw_grade']
        rm_weight = request.POST['raw_weight']
        fm_type = request.POST['fmat_type']
        fm_thickness = request.POST['fmat_thickness']
        fm_size = request.POST['fmat_size']
        fm_weight = request.POST['fmat_weight']
        fm_quantity = request.POST['fmat_quantity']
        fm_scrape = request.POST['fmat_scrape']
        uf_thickness = request.POST['uf_thickness']
        uf_size = request.POST['uf_size']
        uf_weight = request.POST['uf_weight']
        uf_quantity = request.POST['uf_quantity']
        rm = rawMaterial.objects.get(id=rm_id)

        raw_material = rawMaterial.objects.filter(id__exact=rm_id)
        raw_material_data = raw_material.values()
        raw_material_dict = raw_material_data[0]
        raw_material_weight = int(raw_material_dict['RM_coilWeight'])

        if raw_material_weight < int(rm_weight):
            return JsonResponse({'status': 1})
        else:
            user = User.objects.get(id=request.user.id)
            finished_material = FMstock(UF_Weight=uf_weight, coilUID=rm, Size=rm_size, FM_Date=date, Grade=rm_grade, coilWeight=rm_weight, materialType=fm_type,
                                        FM_Thickness=fm_thickness, FM_Size=fm_size, FM_Weight=fm_weight, FM_Quantity=fm_quantity, FM_scrapWeight=fm_scrape,
                                        UF_Thickness=uf_thickness, UF_Size=uf_size, UF_Quantity=uf_quantity, register=user)
            finished_material.save()
            finished_material_value = list(FMstock.objects.values())

            return JsonResponse({'status': 'Save', 'fm_data': finished_material_value})
    else:
        return JsonResponse({'status': 0})

########################################################################

# this function deletes finished material data
@del_access
@unautherized_user
def Finished_Material_Delete(request):
    try:
        if request.method == "POST":
            fm_id = request.POST['sid']
            finished_material = FMstock.objects.get(id=fm_id)
            user = User.objects.get(id=request.user.id)
            logsave.logg(regid=user.id, tbid=fm_id, operation='Entry Deleted', tname='Finished Material Stock')
            finished_material.delete()
            scrape = Scrape.objects.get(t_id = fm_id)
            scrape.delete()
            return JsonResponse({'status': 1})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function gets rm id to fm page
def get_finished_material_type(request, *args, **kwargs):
    selected_id = kwargs.get('id')
    s_type = list(FMstock.objects.filter(id=selected_id).values())
    return JsonResponse({'data': s_type})

########################################################################

# this function saves finsihed material data
@unautherized_user
def Finished_Material_Sale_Save(request):
    if request.method == 'GET':
        fm_stock_val = list(FMstock.objects.values())
        return JsonResponse({'data': fm_stock_val})
    try:
        if request.method == "POST":
            fm_id = request.POST['fmsales_id']
            date = request.POST['sales_date']
            sales_quantity = request.POST['sales_quantity']
            sales_weight = request.POST['sales_weight']
            sale_type = request.POST['sale_type']
            sold_to = request.POST['sold_to']
            fmcoil = FMstock.objects.get(id=fm_id)
            finished_material = FMstock.objects.filter(id__exact=fm_id)
            finished_material_data = finished_material.values()
            finished_material_dic = finished_material_data[0]
            finished_material_weight = int(finished_material_dic['FM_Weight'])
            finished_material_quantity = int(finished_material_dic['FM_Quantity'])

            if finished_material_weight < int(sales_weight):
                return JsonResponse({'status': 1})
            elif finished_material_quantity < int(sales_quantity):
                return JsonResponse({'status': 2})
            else:
                user = User.objects.get(id=request.user.id)
                sale = Sale(register=user, FMcoilUID=fmcoil, Sale_date=date, Sale_Weight=sales_weight,
                            Sale_Quantity=sales_quantity, Stock='Finished Material Stock', Sale_Type=sale_type,To =sold_to)
                sale.save()
                sale_val = Sale.objects.filter(
                    Stock__exact='Finished Material Stock').values()
                sale_data = list(sale_val)
                
                return JsonResponse({'status': 'Save', 'sale_data': sale_data})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function deletes unfinished material data
@del_access
@unautherized_user
def Finished_Material_Sale_Delete(request):
    try:
        if request.method == "POST":
            fm_id = request.POST['sid']
            user = User.objects.get(id=request.user.id)
            logsave.logg(regid=user.id, tbid=fm_id,
                        operation='Sales Entry Deleted', tname='Finished Material Stock')
            fm_sale = Sale.objects.get(id=fm_id)
            fm_sale.delete()
            return JsonResponse({'status': 1})
    except:
        return JsonResponse({'status': 0})

########################################################################

#this function gets ufm id to ufm sale
def get_unfinished_material_type(request, *args, **kwargs):
    selected_id = kwargs.get('id')
    us_type = list(UFMstock.objects.filter(id=selected_id).values())
    return JsonResponse({'data': us_type})

########################################################################

# this function saves unfinished sale data
@unautherized_user
def UnFinished_Material_Sale_Save(request):
    if request.method == 'GET':
        us_id_val = list(UFMstock.objects.values())
        return JsonResponse({'data': us_id_val})
    try:
        if request.method == "POST":
            us_m_type = request.POST['us_m_type']
            ufm_id = request.POST['ufmsales_id']
            date = request.POST['sales_date']
            sales_quantity = request.POST['sales_quantity']
            sales_weight = request.POST['sales_weight']
            sold_to = request.POST['usale_sold']
            ufm_coil = UFMstock.objects.get(id=ufm_id)
            ufm = UFMstock.objects.filter(id__exact=ufm_id)
            ufm_data = ufm.values()
            ufm_dict = ufm_data[0]
            ufm_weight = int(ufm_dict['UFM_Weight'])
            ufm_quantity = int(ufm_dict['UFM_Quantity'])
            if ufm_weight < int(sales_weight):
                return JsonResponse({'status': 1})
            elif ufm_quantity < int(sales_quantity):
                return JsonResponse({'status': 2})
            else:
                user = User.objects.get(id=request.user.id)
                sale = Sale(register=user, UFcoilID=ufm_coil, Sale_date=date, Sale_Weight=sales_weight,
                            Sale_Quantity=sales_quantity, Stock='Un-Finished Material Stock', Sale_Type=us_m_type,To =sold_to)
                sale.save()
                sale_val = Sale.objects.filter(Stock__exact='Un-Finished Material Stock').values()
                sale_data = list(sale_val)
                return JsonResponse({'status': 'Save', 'sale_data': sale_data})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function deletes unfinished sales data
@del_access
@unautherized_user
def UnFinished_Material_Sale_Delete(request):
    '''ufm(Un-finished material)'''
    try:
        if request.method == "POST":
            ufm_id = request.POST['sid']
            user = User.objects.get(id=request.user.id)
            logsave.logg(regid=user.id, tbid=ufm_id, operation='Sales Entry Deleted',
                        tname='Un-Finished Material Stock')
            ufm_sale = Sale.objects.get(id=ufm_id)
            ufm_sale.delete()

            return JsonResponse({'status': 1})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function saves essential material data
@unautherized_user
def Essential_Item_Save(request):
    # try:
    if request.method == "POST":
        es_date = request.POST['es_date']
        es_type = request.POST['es_type']
        es_quantity = request.POST['es_quantity']
        es_size = request.POST['es_size']
        user = User.objects.get(id=request.user.id)
        es = essentialitemStock(
            Type=es_type, ES_Quantity=es_quantity, ES_Size=es_size, ES_Date=es_date, register=user)
        es.save()
        es_value = essentialitemStock.objects.values()
        es_data = list(es_value)
        return JsonResponse({'status': 'Save', 'es_data': es_data})
    else:
        return JsonResponse({'status': 0})

########################################################################

# this function deletes essentiol material data
@del_access
@unautherized_user
def Essential_Item_Delete(request):
    try:
        if request.method == "POST":
            es_id = request.POST['sid']
            essential = essentialitemStock.objects.get(id=es_id)
            user = User.objects.get(id=request.user.id)
            logsave.logg(regid=user.id, tbid=es_id,
                        operation='Entry Deleted', tname='Essential Item Stock')
            essential.delete()
            return JsonResponse({'status': 1})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function gets es id to user per day 
def get_essential_type(request, *args, **kwargs):
    selected_id = kwargs.get('id')
    es_type = list(essentialitemStock.objects.filter(id=selected_id).values())
    return JsonResponse({'data': es_type})

########################################################################

# this functions saves use per day data
@unautherized_user
def Essential_Usage_Save(request):
    if request.method == 'GET':
        essential_data = list(essentialitemStock.objects.values())
        return JsonResponse({'data': essential_data})
    try:
        if request.method == "POST":
            esu_date = request.POST['esu_date']
            esu_type = request.POST['esu_type']
            esu_quantity = request.POST['esu_quantity']
            esu_size = request.POST['esu_size']
            esu_id = request.POST['esu_id']
            es_id = essentialitemStock.objects.get(id=esu_id)
            es = essentialitemStock.objects.filter(id__exact=esu_id)
            es_data = es.values()
            es_dic = es_data[0]
            es_quantity = int(es_dic['ES_Quantity'])
            if es_quantity < int(esu_quantity):
                return JsonResponse({"status": 1})
            user = User.objects.get(id=request.user.id)
            esu = EssentialItemUsePerDay(
                EPD_UID=es_id, EPD_Type=esu_type, EPD_Quantity=esu_quantity, EPD_Size=esu_size, EPD_Date=esu_date, register=user)
            esu.save()
            esu_value = list(EssentialItemUsePerDay.objects.values())
            es_value = list(essentialitemStock.objects.values())
            
            return JsonResponse({'status': 'Save', 'upd_data': esu_value, 'e_data': es_value})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function deletes upd data(use per day data)
@del_access
@unautherized_user
def Essential_Usage_Delete(request):
    try:
        if request.method == "POST":
            esu_id = request.POST['sid']
            esu = EssentialItemUsePerDay.objects.get(id=esu_id)
            user = User.objects.get(id=request.user.id)
            logsave.logg(regid=user.id, tbid=esu_id,
                        operation='Entry Deleted', tname='Essential Item Stock')
            esu.delete()
            return JsonResponse({'status': 1})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function updates user page info
@unautherized_user
def user_save(request):
    try:
        if request.method == "POST":
            user_id = request.POST['u_id']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.get(id=request.user.id)
            register = Register.objects.get(user=user)
            user.set_password(password)
            user.first_name = fname
            user.last_name = lname
            user.email = email
            register.First_Name = fname
            register.Last_Name = lname
            register.UserName = email
            register.save()
            user.save()
            return JsonResponse({'status': 'Save'})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function updates data
@unautherized_user
def user_delete(request):
    try:
        if request.method == "POST":
            user_id = request.POST['sid']
            # user = User.objects.get()
            register = Register.objects.get(id=user_id)
            user = register.UserName
            user = User.objects.get(username=user)
            register.delete()
            user.delete()
            return JsonResponse({'status': 1})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this is our logout data
def Logout(request):
    logout(request)
    return redirect('login')

########################################################################

#this function saves register page info
@unauthenticated_user
def register(request):
    if request.method == 'POST':
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        username = request.POST['email']
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password2, first_name=fname, last_name=lname)
                user.save()
                registered_user = Register.objects.create(user=user, First_Name=fname, Last_Name=lname, UserName=username, delete_access='False')
                registered_user.save()
                alertmessages.empty(subject='Account Created',
                                    text=username, stock_count='')
                messages.success(request, 'You are now registered and can log in')
                return redirect('login')
        else:
            messages.error(request, 'Error!, Passwords do not match')
            return redirect('register')
    return render(request, 'auth/register.html')

########################################################################

# this function save timmer info
@unautherized_user
def Set_Timer(request):
    try:
        if request.method == "POST":
            a_time = request.POST['ac_time']
            d_time = request.POST['dc_time']
            timer = Timmer.objects.create()
            timer.active_time = a_time
            timer.inactive_time = d_time
            timer.save()
            timer_value = list(Timmer.objects.values())
            return JsonResponse({'status': 'Save', 'timmer_data': timer_value})
    except:
        return JsonResponse({'status': 0})

########################################################################

# this function save role/stauts/delete access data
def Employee_Access(request):
    # try:
    if request.method == "POST":
        role = request.POST['rl']
        status = request.POST['st']
        del_access = request.POST['del_access']
        user_id = request.POST['sid']
        register = Register.objects.get(id=user_id)
        register.status = status
        register.userRole = role
        register.delete_access = del_access
        register.save()
        return JsonResponse({"status": 'Save'})
# except:
    else:
        return JsonResponse({"status": 0})

########################################################################

# this is our notification alert system
def Notification_Alert(request):
    try:
        # if request.method == 'POST':
        b = request.GET['button']
        if b == 'clicked':
            msg = Messages.objects.values()
            for i in msg:
                msg_id = i['id']
                message = Messages.objects.get(id=msg_id)
                message.seen = 'True'
                message.save()
        return JsonResponse({'status': 'Save'})
    except:
        return JsonResponse({'status': 0})


# Displaying 404 Page in Production
#  Dispaly 404 page if the response is not visible
def error_404(request, exception):
        data = {}
        return render(request,'error404.html', data)

def error_500(request):
        data = {}
        return render(request,'error404.html', data)

def raw_material_graph(request):
    if request.is_ajax and request.method == 'GET':
        raw_material_data = rawMaterial.objects.values()
        # extracting grade and coilweight from filtered data
        raw_material_coilweight = extracting_data_for_graph.dictionary(dic=raw_material_data, key='RM_Grade', value='RM_coilWeight')
        # dumping extracted data    
        raw_material_coilweight_dict = json.dumps(raw_material_coilweight)
        # laoding data
        raw_material_coilweight_graph = json.loads(raw_material_coilweight_dict)
    return JsonResponse({'status':raw_material_coilweight_graph})
    