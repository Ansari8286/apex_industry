
import pandas as pd
import datetime
import csv
from fpdf import FPDF
# def timmer():
#     my_time = 0
#     for i in range(24):
#         my_time += 1
#         print(my_time,'time')
        
#         print(my_time)
#         all_users = [{'id': 6, 'user_id': 30, 'Name': 'Shashank Kumar', 'UserName': 'zombiebaloon@gmail.com', 'status': 'pending', 'userRole': 'Active'}, {'id': 7, 'user_id': 37, 'Name': None, 'UserName': 'zombiebaloon000@gmail.com', 'status': 'Pending', 'userRole': 'Active'}, {'id': 8, 'user_id': 38, 'Name': None, 'UserName': 'zombiebaloon007@gmail.com', 'status': 'Pending', 'userRole': 'Active'}, {'id': 9, 'user_id': 39, 'Name': None, 'UserName': 'user@gmail.com', 'status': 'Pending', 'userRole': 'Active'}, {'id': 10, 'user_id': 40, 'Name': None, 'UserName': 'user2@gmail.com', 'status': 'Pending', 'userRole': 'Active'}, {'id': 11, 'user_id': 41, 'Name': None, 'UserName': 'user3@gmail.com', 'status': 'Pending', 'userRole': 'Not_Active'}]
#         if my_time >=8 and my_time <= 20:
#             for i in all_users:
#                 i['userRole'] = 'Active'
#                 print(i['userRole'],'working hours')
#         elif my_time > 20 or my_time < 8:
#             for i in all_users:
#                 i['userRole'] = 'Not_Active'
#                 print(i['userRole'],'working hours over')
# while True:
#     time.sleep
#     timmer()
class PDF(FPDF):
    def header(self):
#         self.image()
        page_width = self.w - 2 * self.l_margin
        self.set_font('Times','B',14)
        self.cell(page_width,0.0,'Daily Report',align = 'C')
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica','I',10)
        #page number
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}',align= 'C')
    def body_title(self,page_title):
        self.set_font('helvetica','',12)
        p_title = f'{page_title}'
        self.cell(0,5,p_title,ln=True)
        self.ln()
    def body(self, name):
        #reading
        self.set_font('Courier','',12)
        page_width = self.w - 2 * self.l_margin
        col_width = page_width/6
        self.ln(1)
        th= self.font_size
        with open(name, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                self.cell(10,th,str(row[0]),border=1)
                self.cell(30,th,row[1],border=1)
                self.cell(28,th,row[2],border=1)
                self.cell(25,th,row[3],border=1)
                self.cell(23,th,row[4],border=1)
                self.cell(17,th,row[5],border=1)
                self.cell(30,th,row[6],border=1)
                self.cell(35,th,row[7],border=1)
                self.ln(th)

        self.ln(10)
        self.set_font('Times','',10.0) 
        self.cell(page_width, 0.0, '- end of report -', align='C')
        
    def print_page(self,page_title,name):
        self.add_page()
        self.body_title(page_title)
        self.body(name)



class Fetch_Data:
    def raw_material(rm_data):
        RM_Data = rm_data
        id_list = []
        register_id = []
        Date =[]
        RM_thickness=[]
        RM_Size = []
        RM_Grade = []
        RM_coilweight = []
        RM_Scrapweight = []
        for i in RM_Data.values():
            id_list.append(i['id'])
            register_id.append(i['register_id'])
            Date.append(i['RM_Date'])
            RM_thickness.append(i['RM_Thickness'])
            RM_Grade.append(i['RM_Grade'])
            RM_Size.append(i['RM_Size'])
            RM_coilweight.append(i['RM_coilWeight'])
            RM_Scrapweight.append(i['RM_scrapWeight'])
        Raw_dic = {
            'id': id_list,
            'register id': register_id,
            'Date':Date,
            'Thickness': RM_thickness,
            'Grade': RM_Grade,
            'Size': RM_Size,
            'Weight': RM_coilweight,
            'ScrapeWeight': RM_Scrapweight
        }
        return Raw_dic
    def EssentialitemUserperDay(es_data):
        Date = []
        ES_Data = es_data
        # FM_dic = FM_Data.values()
        es_id = []
        Register_id = []
        Type = []
        Size = []
        EPD_uid = []
        Quantity = []

        for i in ES_Data.values():
            es_id.append(i['id'])
            Type.append(i['EPD_Type'])
            Date.append(i['EPD_Date'])
            Register_id.append(i['register_id'])
            EPD_uid.append(i['EPD_UID_id'])
            Size.append(i['EPD_Size'])
            Quantity.append(i['EPD_Quantity'])
        ES_dic = {
            'extra': 0,
            'id': es_id,
            'Item Stock id': EPD_uid,
            'Date': Date,
            'Register':Register_id,
            'Type': Type,
            'Size':Size,
            'Quantity': Quantity,
        }
        return ES_dic


    # def fm_stock(fm_data):
    #     Date = []
    #     FM_Data = fm_data
    #     # FM_dic = FM_Data.values()
    #     FM_id = []
    #     Register_id = []
    #     CoilUID = []
    #     Size = []
    #     Grade = []
    #     CoilWeight = []
    #     MaterialType = []
    #     FM_Thickness = []
    #     FM_Size = []
    #     FM_Weight = []
    #     FM_Quantity = []
    #     FM_scrapWeight = []
    #     UF_Thickness = []
    #     UF_Size = [] 
    #     UF_Weight = []
    #     UF_Quantity = []

    #     for i in FM_Data.values():
    #         FM_id.append(i['id'])
    #         Date.append(i['FM_Date'])
    #         Register_id.append(i['register_id'])
    #         CoilUID.append(i['coilUID_id'])
    #         Size.append(i['Size'])
    #         Grade.append(i['Grade'])
    #         CoilWeight.append(i['coilWeight'])
    #         MaterialType.append(i['materialType'])
    #         FM_Thickness.append(i['FM_Thickness'])
    #         FM_Size.append(i['FM_Size'])
    #         FM_Weight.append(i['FM_Weight'])
    #         FM_Quantity.append(i['FM_Quantity'])
    #         FM_scrapWeight.append(i['FM_scrapWeight'])
    #         UF_Thickness.append(i['UF_Thickness'])
    #         UF_Size.append(i['UF_Size'])
    #         UF_Weight.append(i['UF_Weight'])
    #         UF_Quantity.append(i['UF_Quantity'])
    #     FM_dic = {
    #         'id': FM_id,
    #         'Date': Date,
    #         'Register':Register_id,
    #         'Coil': CoilUID,
    #         'Size':Size,
    #         'Grade':Grade,
    #         'Weight': CoilWeight,
    #         'Material Type': MaterialType,
    #         'FM Thickness': FM_Thickness,
    #         'FM Size': FM_Size,
    #         'FM Quant': FM_Quantity,
    #         'FM ScrapW': FM_scrapWeight,
    #         'UF Thickness': UF_Thickness,
    #         'UF Size': UF_Size,
    #         'UF Weight':UF_Weight,
    #         'UF Quan': UF_Quantity
    #     }
    #     return FM_dic
