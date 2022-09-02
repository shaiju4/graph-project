from ast import Pass
from enum import unique
from itertools import count
import re
from tkinter import NO
# from audioop import reverse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.core.files.storage import FileSystemStorage
import pandas as pd
import openpyxl
from django.contrib import messages

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from rest_framework.views import APIView 

from django.http import HttpResponse, JsonResponse
import json
import xlrd
import csv

@csrf_exempt
def index(request):
    print(request)
    if request.method=="POST":
        file_name=request.POST['filename']
        file=request.FILES.get('file')
        print(file_name)
        date=request.POST['date']
        obj=File()
        obj.file=file
        obj.table_name=file_name
        obj.date=date
        obj.save()
        read_file = pd.read_excel(file)
        read_file.to_csv (f'media/csv/{file_name}.csv', index = None, header=True)
        file=open(f'media/csv/{file_name}.csv',mode='r')
        data=file.readlines()
        if file_name=='current_employees':
            Model=Currentemployees()
            print(type(Model))
        else:
            Model=Resignedemployees()
            print(type(Model))
        my_list=[]
        for i in range(len(data)):
            values=data[i].split(',')
            my_list.append(values)
        
        my_list.remove(my_list[0])
        
        for i in range(len(my_list)):
            flag=True
            try:
                if file_name=='current_employees':
                    details=Currentemployees.objects.get(Emp_Code=my_list[i][0])
                    flag=False
                else:
                    details=Resignedemployees.objects.get(Emp_Code=my_list[i][0])
                    flag=False
                   
            except:
                print('except')
                pass
            if flag==False:
                if file_name=='current_employees':
                    Currentemployees.objects.filter(Emp_Code=my_list[i][0]).update(Emp_Name=my_list[i][1],Joining_Date=my_list[i][2],Division=my_list[i][3],
                    Rel_Exp_Till_Date_in_Yrs=round(float(my_list[i][4])),Designation=my_list[i][5],Date_of_Birth=my_list[i][6].split(' ')[0],
                    Project_Function=my_list[i][7],QA_Dev_DB=my_list[i][8],Gender=my_list[i][9],Source=my_list[i][10],
                    Full_Time_Contractual=my_list[i][11],Manager_Name=my_list[i][12])
                else:
                    Resignedemployees.objects.filter(Emp_Code=my_list[i][0]).update(Emp_Name=my_list[i][1],Joining_Date=my_list[i][2],Division=my_list[i][3],
                    Rel_Exp_Till_Date_in_Yrs=round(float(my_list[i][4])),Designation=my_list[i][5],Date_of_Birth=my_list[i][6].split(' ')[0],
                    Project_Function=my_list[i][7],QA_Dev_DB=my_list[i][8],Gender=my_list[i][9],Source=my_list[i][10],
                    Full_Time_Contractual=my_list[i][11],Manager_Name=my_list[i][12])

            else:
                if file_name=='current_employees':
                   obj=Currentemployees()
                else:
                    obj=Resignedemployees()
                obj.Emp_Code=my_list[i][0]
                obj.Emp_Name=my_list[i][1]
                obj.Joining_Date=my_list[i][2]
                obj.Division=my_list[i][3]
                obj.Rel_Exp_Till_Date_in_Yrs=round(float(my_list[i][4]))
                obj.Designation=my_list[i][5]
                obj.Date_of_Birth=my_list[i][6].split(' ')[0]
                obj.Project_Function=my_list[i][7]
                obj.QA_Dev_DB=my_list[i][8]
                obj.Gender=my_list[i][9]
                obj.Source=my_list[i][10]
                obj.Full_Time_Contractual=my_list[i][11]
                obj.Manager_Name=my_list[i][12]
                obj.save()
        
               
            
        files=File.objects.all()
        last_ten = File.objects.all().order_by('-file_id')[:5]
        messages.success(request,'file uploaded successfully')
        print(len(files))
        return render(request,'index.html',{'details':last_ten,'length':len(files)})
    else:
        files=File.objects.all()
        last_ten = File.objects.all().order_by('-file_id')[:5]
        
        return render(request,'index.html',{'details':last_ten,'length':len(files)})

def write_csv():
    
    file=open('media/updated_csv/current_employees.csv',mode='a')
    file1=open('media/updated_csv/resigned_employees.csv',mode='a')
    writer = csv.writer(file)
    writer.writerow(['Emp_Code','Emp_Name','Joining_Date','Division','Rel_Exp_Till_Date_in_Yrs','Designation','Date_of_Birth','Project_or_Function','QA_Dev_DB','Gender','Source','Full_Time_or_Contractual','Manager_Name'])

    writer1 = csv.writer(file1)
    writer1.writerow(['Emp_Code','Emp_Name','Joining_Date','Division','Rel_Exp_Till_Date_in_Yrs','Designation','Date_of_Birth','Project_or_Function','QA_Dev_DB','Gender','Source','Full_Time_or_Contractual','Manager_Name'])

    Current = Currentemployees.objects.all().values_list('Emp_Code','Emp_Name','Joining_Date','Division','Rel_Exp_Till_Date_in_Yrs','Designation','Date_of_Birth','Project_or_Function','QA_Dev_DB','Gender','Source','Full_Time_or_Contractual','Manager_Name')
    resigned = Resignedemployees.objects.all().values_list('Emp_Code','Emp_Name','Joining_Date','Division','Rel_Exp_Till_Date_in_Yrs','Designation','Date_of_Birth','Project_or_Function','QA_Dev_DB','Gender','Source','Full_Time_or_Contractual','Manager_Name')
    for user in Current:
        writer.writerow(user) 
    for user in resigned:
        writer1.writerow(user)
    
    





@csrf_exempt
def query(request):
    if request.method=="POST":
        table=request.POST['table']
        print(table)
        per=request.POST['per']
        print(per)
        try:
            start_date=request.POST['startdate']
            end_date=request.POST['enddate']
            print(start_date,end_date)
        except:
            pass
           
        trend=request.POST['trend']
        
        aggregation=request.POST['aggregation']
        groupby=request.POST['groupby']
        trendby=request.POST['trendby']
        condition=request.POST['condition']
        date=request.POST['date']
        
        
        if groupby==''or per==''or trend==''or aggregation =='':
            messages.error(request,'please select all field')
            return redirect('que')
        else:
            print(table,'asghetjrystdu')
            table1=File.objects.filter(date=date,table_name=table).values()
            print(table1)
            if len(table1)==0:
                messages.error(request,'No table is in this date')
                return redirect('que')
            print(len(table1),'aegerhetssrtj')
            print(table1[0]['file'])
            files=File.objects.all()
        
           
            if table=='current_employees':
               
                if per=='other':
                   
                    values=Currentemployees.objects.raw(f"SELECT id ,{groupby} as position,EXTRACT(month FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '{start_date}' and '{end_date}')and  {trendby} ='{condition}' GROUP BY {groupby}")

                else:
                   
                    # values=Currentemployees.objects.raw(f"SELECT id ,{groupby} as position,EXTRACT({per} FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees  GROUP BY {groupby},EXTRACT({per} FROM joining_date)")
                    values=Currentemployees.objects.raw(f"SELECT id ,{groupby} as position,EXTRACT({per} FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE {trendby} ='{condition}'  GROUP BY {groupby}")
            else:
                if per=='other':
                    values=Currentemployees.objects.raw(f"SELECT id ,{groupby} as position,EXTRACT(month FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '{start_date}' and '{end_date}')and  {trendby} ='{condition}' GROUP BY {groupby}")
                else:
                    values=Resignedemployees.objects.raw(f"SELECT id ,{groupby} as position,EXTRACT({per} FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE {trendby} ='{condition}'  GROUP BY {groupby}")

            emp_count=[]
            duration=[]
            position=[]
            for i in values:
                emp_count.append(i.emp_count)
                duration.append(i.duration)
                position.append(i.position.strip())
                print(i.position)
            print((emp_count))
            print(set(duration))
            unique_duration=set(duration)
           
            print(set(position))
            data=[]
            for i in values:
                for j in range(len(unique_duration)):
                    if i.duration==list(unique_duration)[j]:
                        data.append({'y':i.duration,'a':i.emp_count,'b':i.position.strip()})
            print(data)
            print(len(unique_duration),'len of unique_duration')
            print(len(data),'len of data')
            if len(data)==0:
                messages.error(request,'Invalid syntax or no data')
                return redirect('que')
            final_data=[]
            for i in range(len(unique_duration)):
                final_data.append({})
            
            
            for i in range(len(data)):
                for j in range(len(unique_duration)):
                    final_data[j].update({"year":f"month {list(unique_duration)[j]}"})
                    if data[i]['y']==duration[j]:
                        for z in range(len(position)):
                            if data[i]['b']==position[z]:
                                final_data[j].update({f'{position[z]}':data[i]['a']})
            
            
            unique_position=set(position)
            
            context = {'segment': 'charts_from_file','details':files,'chart':True} 
            context['chart_data']=json.dumps({
            "element": "morris-bar-chart",
            "data":final_data,
            "xkey": "year",
            "barSizeRatio": 0.70,
            "barGap": 3,
            "resize": True,
            "responsive": True,
            "ykeys": [f'{list(unique_position)[i]}' for i in range(len(unique_position))],
            "labels": list(unique_position),
            "barColors": ["0-#1de9b6-#1dc4e9", "0-#899FD4-#A389D4", "#04a9f5"]
            })
            return render(request,'query.html',(context))  
        


    else:
        files=File.objects.all()
        context = {'segment': 'charts_from_file','details':files}
        context['chart_data']=json.dumps({
        "element": "morris-bar-chart",
        "data": [
            { "y": "2017", "a": "150", "b": "90", "c": "80" },
            { "y": "2018", "a": "220", "b": "350", "c": "50" },
            { "y": "2019", "a": "80", "b": "300", "c": "240" },
            { "y": "2020", "a": "180", "b": "30", "c": "10" }
        ],
        "xkey": "y",
        "barSizeRatio": 0.70,
        "barGap": 3,
        "resize": True,
        "responsive": True,
        "ykeys": ["a", "b", "c"],
        "labels": ["Product A", "Product B", "Product C"],
        "barColors": ["0-#1de9b6-#1dc4e9", "0-#899FD4-#A389D4", "#04a9f5"]
        })
        return render(request,'query.html',(context))
        





def csv_from_excel(name,staff):
    wb = xlrd.open_workbook(name)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(f'{staff}.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()






@csrf_exempt  
def get_column(request):
   
    table=request.POST.get('table')
    print(table)
    
    print(table)
    name=f'media/csv/{table}.csv'
    if '.csv' in name:
        df=pd.read_csv(name)
        data_set=[]
        for i in df.columns:
            data={
                'columns':i
            }
            data_set.append(data)
        print(data_set[2:],'iiiiiiiiiiiiiiiiiiiiiiiiiii')
        print(data_set)
        return JsonResponse(json.dumps(data_set),content_type='application/json', safe=False)
    else:
        df=pd.read_excel(table.file)
        data_set=[]
        for i in df.columns:
            data={
                'columns':i
            }
            data_set.append(data)
        print(data_set[2:],'iiiiiiiiiiiiiiiiiiiiiiiiiii')
        return JsonResponse(json.dumps(data_set), content_type='application/json', safe=False)
    





def chart(request):
    df=pd.read_csv('your_csv_file.csv')
    print(df['Emp Code'])

    return render(request,'chart.html',{'df':df['Emp Code']})
  
def current(request):
    values=Currentemployees.objects.raw(f"SELECT id ,Project_or_Function as position,EXTRACT(quarter FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees  GROUP BY Project_or_Function,EXTRACT(quarter FROM joining_date)")

    emp_count=[]
    duration=[]
    position=[]
    for  i in values:
        emp_count.append(i.emp_count)
        duration.append(i.duration)
        position.append(i.position.strip())
    pie_data=[['Gender', 'Count'],
    ]
    position1=set(position)
    # print(position)
    for i in range(len(position1)):
        pie_data.append([])
    for i in range(len(position1)):
        pie_data[i+1].append(list(position1)[i])
        pie_data[i+1].append(emp_count[i])
    context = {'segment': 'charts_from_file',"pie_data":pie_data}
    with open('graph/charts_morris.json', 'r') as f:
        context['chart_data'] = json.dumps(json.load(f))
    
    return render(request,'current_employees.html',(context))


def resigned(request):
    context = {'segment': 'charts_from_file',"type":'resigned'}
    with open('graph/charts_morris.json', 'r') as f:
        context['chart_data'] = json.dumps(json.load(f))
    
    
    return render(request,'resigned_employees.html',(context))


@csrf_exempt
def bar(request):
    
    type='current'
    try:
        type1=request.POST['type']
        type=type1
        start_date=request.POST['startdate']
        end_date=request.POST['enddate']
        print(start_date,end_date,'iiiiiiiiiiiiiiiiiii')
    except:
        pass
   
    if type=='current':
        files=Currentemployees.objects.all()
        if len(files)==0:
            return render(request,'barchart.html',{'files':len(files)})
    else:
        files=Resignedemployees.objects.all()
        if len(files)==0:
            print('hiiiiiiiiiiiiiiiiiiiii')
            return render(request,'barchart.html',{'files':len(files)})

    try:
        value=request.POST['value']
        # print(value)
    except:
        pass
   
    print(value,'monthhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
    
    if type=='resigned':
        table='media/updated_csv/resigned_employees.csv'
    else:
        table='media/updated_csv/current_employees.csv'
    
   
    type='current'
    try:
        type1=request.POST['type']
        type=type1
        start_date=request.POST['startdate']
        end_date=request.POST['enddate']
    except:
        pass
   
    if type=='current':
        files=Currentemployees.objects.all()
        if len(files)==0:
            return render(request,'barchart.html',{'files':len(files)})
    else:
        files=Resignedemployees.objects.all()
        if len(files)==0:
            return render(request,'barchart.html',{'files':len(files)})

    try:
        value=request.POST['value']
        print(value)
    except:
        pass
   
    print(value)
    
    if type=='current':
        if value=='nothing':
            
            values=Currentemployees.objects.raw(f"SELECT id ,Project_or_Function as position,EXTRACT(month FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '{start_date}' and '{end_date}') GROUP BY Project_or_Function")
            # values=Currentemployees.objects.raw("SELECT id ,Project_or_Function as position,EXTRACT(month FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '2021-06-01' and '2021-08-01')and Project_or_Function ='management' GROUP BY Project_or_Function")
            value='month'
            
        else:
            values=Currentemployees.objects.raw(f"SELECT id ,Project_or_Function as position,EXTRACT({value} FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees  GROUP BY Project_or_Function,EXTRACT({value} FROM joining_date)")
    else:
        if value=='nothing':
            values=Resignedemployees.objects.raw(f"SELECT id ,Project_or_Function as position,EXTRACT(year FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '{start_date}' and '{end_date}') GROUP BY Project_or_Function")
            value='date'

        else:
            values=Resignedemployees.objects.raw(f"SELECT id ,Project_or_Function as position,EXTRACT({value} FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees  GROUP BY Project_or_Function,EXTRACT({value} FROM joining_date)")
    
    
    emp_count=[]
    duration=[]
    position=[]
    for i in values:
        emp_count.append(i.emp_count)
        duration.append(i.duration)
        position.append(i.position.strip())
        print(i.position)
    print((emp_count))
    print(set(duration))
    unique_duration=set(duration)
    
    print(set(position))
    data=[]
    for i in values:
        for j in range(len(unique_duration)):
            if i.duration==list(unique_duration)[j]:
                data.append({'y':i.duration,'a':i.emp_count,'b':i.position.strip()})
    print(data,'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    print(len(unique_duration),'len of unique_duration')
    print(len(data),'len of data') 
    final_data=[]
    for i in range(len(unique_duration)):
        final_data.append({})
    
    
    for i in range(len(data)):
        for j in range(len(unique_duration)):
            final_data[j].update({"year":f"{value} {list(unique_duration)[j]}"})
            if data[i]['y']==duration[j]:
                for z in range(len(position)):
                    if data[i]['b']==position[z]:
                        final_data[j].update({f'{position[z]}':data[i]['a']})
    print(final_data)
    
    unique_position=set(position)
    context = {'segment': 'charts_from_file','details':files,'type':type,'chart':True} 
    context['chart_data']=json.dumps({
    "element": "morris-bar-chart1",
    "data":final_data,
    "xkey": "year",
    "barSizeRatio": 0.70,
    "barGap": 3,
    "resize": True,
    "responsive": True,
    "ykeys": [f'{list(unique_position)[i]}' for i in range(len(unique_position))],
    "labels": list(unique_position),
    "barColors": ["0-#1de9b6-#1dc4e9", "0-#899FD4-#A389D4", "#04a9f5"]
    })
    return render(request,'barchart.html',(context))
    

#SELECT id ,Project_or_Function as position,EXTRACT(year FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '01-01-2021' to '26-06-2022') GROUP BY Project_or_Function,EXTRACT(year FROM joining_date)
# SELECT id ,Designation as position,EXTRACT(year FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '2021-01-01' and '2022-01-01') GROUP BY Designation,EXTRACT(year FROM joining_date)





def new(request):
    context = {'segment': 'charts_from_file',"type":'resigned'}
    with open('graph/new.json', 'r') as f:
        context['chart_data'] = json.dumps(json.load(f))
    
    return render(request,'new.html',(context))


def piechart(request,string):
    print(string,'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiihhhhhhhhhhhhhhhhhhhhhhhhhhh')
    # print(request.method)
    start_date=''
    end_date=''
    try:
        
        start_date=request.POST['startdate']
        end_date=request.POST['enddate']
        request.session['start_date']=start_date
        request.session['end_date']=end_date
    except:
        pass
    print(start_date)
    if start_date=='':
        # print('yes')
        values=Currentemployees.objects.raw(f"SELECT id ,Gender as position,EXTRACT(year FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees  GROUP BY Gender,EXTRACT(month FROM joining_date)")

    else:
        values=Currentemployees.objects.raw(f"SELECT id ,Project_or_Function as position,EXTRACT(month FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '{start_date}' and '{end_date}') GROUP BY Project_or_Function")
    query_output=[]
    for i in values:
        query_output.append({'duration':i.duration,'position':i.position,'emp_count':i.emp_count})
    print(query_output)
    emp_count=[]
    duration=[]
    position=[]
    for  i in values:
        emp_count.append(i.emp_count)
        duration.append(i.duration)
        position.append(i.position.strip())
    duration=list(set(duration))
    position=list(set(position))
    my_data=[]
    for i in range(len(position)):
        my_data.append([])
    for i  in query_output:
        for j in range(len(position)):
                if i['position']==position[j]:
                    try:
                        my_data[j].append(i)
                    except:
                        pass
    for i in range(len(my_data)):
        for j in my_data[i]:
            sub_dur=[j['duration']for j in my_data[i]]
            uni=list(set(duration) - set(sub_dur))
            for z in range(len(uni)):
                if uni[z] not in sub_dur:
                    my_data[i].append({'duration':uni[z],'position':j['position'],'emp_count':0})
    filter_data=[]
    for i in range(len(emp_count)):
        filter_data.append([])

    for i in range(len(filter_data)):
        # filter_data[i].insert(0,duration[i])
        try:
            for j in range(len(duration)):
                # filter_data[i].insert(0,duration[i])
                for z in range(len(duration)):
                    if my_data[i][j]['duration']==duration[z]:
                        filter_data[z].append(my_data[i][j]['emp_count'])
                        filter_data[z].append(my_data[i][j]['emp_count'])

        except:
            pass
    for i in range(len(duration)):
        filter_data[i].insert(0,duration[i])

    
    role=[]
    for i in position:
        role.insert(len(role),i)
        role.insert(len(role),{'role':'annotation'})
    role.insert(0,'year')
    filter_data.insert(0,role)
    
    final_data=[]
    for j in filter_data:
        if len(j)==0:
            break
        final_data.append(j)
        
        
           
          
    
    pie_data=[['Employee', 'Count'],
    ]
    position1=set(position)
    # print(position)
    for i in range(len(position1)):
        pie_data.append([])
    for i in range(len(position1)):
        pie_data[i+1].append(list(position1)[i])
        pie_data[i+1].append(emp_count[i])
    # print('dsafdghjiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    print(final_data)
    return render(request,'piechart.html',{'chart_data':final_data,'pie_data':pie_data,'start_date':start_date,'end_date':end_date})

def bar_duration(request):
    print('yesssssssssssssssssssssssssssssssssssssssssssss')
    
    try:
        start_date=request.session['startdate']
        end_date=request.session['enddate']
    except:
        request.method='POST'
        messages.error(request,'no date selected ')
        return redirect('pie_chart')
    print(start_date)
    duration=request.POST['value']
    values=Currentemployees.objects.raw(f"SELECT id ,Project_or_Function as position,EXTRACT({duration} FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees WHERE(joining_date BETWEEN '{start_date}' and '{end_date}') GROUP BY Project_or_Function")
    query_output=[]
    for i in values:
        query_output.append({'duration':i.duration,'position':i.position,'emp_count':i.emp_count})
    emp_count=[]
    duration=[]
    position=[]
    for  i in values:
        emp_count.append(i.emp_count)
        duration.append(i.duration)
        position.append(i.position.strip())
    
    duration=list(set(duration))
    position=list(set(position))
   
    my_data=[]
    for i in range(len(position)):
        my_data.append([])
    for i  in query_output:
        for j in range(len(position)):
                if i['position']==position[j]:
                    try:
                        my_data[j].append(i)
                    except:
                        pass
    for i in range(len(my_data)):
        for j in my_data[i]:
            sub_dur=[j['duration']for j in my_data[i]]
            uni=list(set(duration) - set(sub_dur))
            for z in range(len(uni)):
                if uni[z] not in sub_dur:
                    my_data[i].append({'duration':uni[z],'position':j['position'],'emp_count':0})
        

    # print(my_data)
    filter_data=[]
    for i in range(len(emp_count)):
        filter_data.append([])

    for i in range(len(filter_data)):
        # filter_data[i].insert(0,duration[i])
        try:
            for j in range(len(duration)):
                # filter_data[i].insert(0,duration[i])
                for z in range(len(duration)):
                    if my_data[i][j]['duration']==duration[z]:
                        filter_data[z].append(my_data[i][j]['emp_count'])
                        filter_data[z].append(my_data[i][j]['emp_count'])

        except:
            pass
    for i in range(len(duration)):
        filter_data[i].insert(0,duration[i])

    
    role=[]
    for i in position:
        role.insert(len(role),i)
        role.insert(len(role),{'role':'annotation'})
    role.insert(0,'year')
    filter_data.insert(0,role)
    
    final_data=[]
    for j in filter_data:
        if len(j)==0:
            break
        final_data.append(j)
        
    return JsonResponse(final_data,safe=False)


def pay_summary(request,string):
    print(string)
    













