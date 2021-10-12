from django.urls import path
from .views import *

urlpatterns = [
    # This is authentication part
    path('',Login,name='login'),
    path('Register/',register, name='register'),
    path('logout/',Logout, name='logout'),
    path('user_save',user_save,name='user_save'),
    path('user_delete',user_delete,name='user_delete'),
    path('User-Account/',Account,name='user_account'),
    path('Employee_Access',Employee_Access,name='Employee_Access'),

    path('Set_Timer',Set_Timer,name='Set_Timer'),
    path('Notifcation_Send',Notifcation_Send,name='Notifcation_Send'),
    path('Notification_Alert/',Notification_Alert,name='Notification_Alert'),

    # For overview
    path('Admin-Dashboard/',Admin_Dashboard,name='admin_dashboard'),

    # For raw material
    path('Raw-Material-Stock/',User_Raw_Material,name='user_raw_material'),
    path('Raw-Material-Stock/Raw_Material_Save',Raw_Material_Save,name='Raw_Material_Save'),
    path('Raw-Material-Stock/Raw_Material_Delete',Raw_Material_Delete,name='Raw_Material_Delete'),
    path('raw_material_graph/',raw_material_graph,name='raw_material_graph'),

    # For finished material
    path('Finished-Material-Stock/',User_Finished_Material,name='user_finished_material'),
    path('Finished_Material_Save',Finished_Material_Save,name='Finished_Material_Save'),
    path('Finished_Material_Delete',Finished_Material_Delete,name='Finished_Material_Delete'),
    path('Finished-Material-Stock/Finished_Material_Sale_Save',Finished_Material_Sale_Save,name='Finished_Material_Sale_Save'),
    path('Finished-Material-Stock/Finished_Material_Sale_Delete',Finished_Material_Sale_Delete,name='Finished_Material_Sale_Delete'),

    # For unfinished material
    path('Un-Finished-Material-Stock/',User_UnFinished_Material,name='user_unfinished_material'),
    path('Unfinished_Material_Save',Unfinished_Material_Save,name='Unfinished_Material_Save'),
    path('Un-Finished-Material-Stock/Unfinished_Material_Delete',Unfinished_Material_Delete,name='Unfinished_Material_Delete'),
    path('Un-Finished-Material-Stock/UnFinished_Material_Sale_Save',UnFinished_Material_Sale_Save,name='UnFinished_Material_Sale_Save'),
    path('Un-Finished-Material-Stock/UnFinished_Material_Sale_Delete',UnFinished_Material_Sale_Delete,name='UnFinished_Material_Sale_Delete'),

    # For essential items
    path('Essential-Item-Stock/',User_Essential_Material,name='user_essential_material'),
    path('Essential-Item-Stock/Essential_Item_Save',Essential_Item_Save,name='Essential_Item_Save'),
    path('Essential-Item-Stock/Essential_Item_Delete',Essential_Item_Delete,name='Essential_Item_Delete'),
    path('Essential-Item-Stock/Essential_Usage_Save',Essential_Usage_Save,name='Essential_Usage_Save'),
    path('Essential-Item-Stock/Essential_Usage_Delete',Essential_Usage_Delete,name='Essential_Usage_Delete'),

    # This is for dependent dropdowns
    path('Essential-Item-Stock/get_essential_type/<str:id>/',get_essential_type,name='get_essential_type'),
    path('Finished-Material-Stock/get_raw_material_grade/<str:id>/',get_raw_material_grade,name='get_raw_material_grade'),
    path('Finished-Material-Stock/get_finished_material_type/<str:id>/',get_finished_material_type,name='get_finished_material_type'),
    path('Un-Finished-Material-Stock/get_unfinished_material_type/<str:id>/',get_unfinished_material_type,name='get_unfinished_material_type'),
]