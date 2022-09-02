#////////////////////////custom chart static///////////////////////////////


# @csrf_exempt
# def test(request):
    
#     type='current'
#     try:
#         type1=request.POST['type']
#         type=type1
#         print(type,'wegarethhughohreioghoieroigheiorsihiareijghioejri')
#     except:
#         pass



#     value='month'
  
#     try:
#         value1=request.POST['value']
#         value=value1
#         print(value,'wegarethhughohreioghoieroigheiorsihiareijghioejri')
#     except:
#         pass
#     print(value)
    
#     if type=='resigned':
#         table=File.objects.get(table_name='resigned_employees')
#     else:
#         table=File.objects.get(table_name='current_employees')

#     file_name=str(table.file)
#     print(file_name)
#     if 'csv' in file_name:
#         name=f'media/{table.file}'
#         df=pd.read_csv(name)
#         print(df['Project/Function'].unique())
#     else:
#         files=File.objects.all()
#         name=f'media/{table.file}'
#         df=pd.read_excel(name)
#         group=df['Project/Function'].unique()
#         if value=='year':
#             year=df.Joining_Date.dt.year
#             print(year)
#             x = np.array(year)
#             y=list(np.unique(x))
#             distinct_date=[]
#             for i in y:
#                 distinct_date.append(i)
#         elif value=='quarter':
#             quarter=df.Joining_Date.dt.quarter
#             x = np.array(quarter)
#             y=list(np.unique(x))
#             distinct_date=[]
#             for i in y:
#                 distinct_date.append(i)
#         else:
#             month=df.Joining_Date.dt.month
#             print(month)
#             x = np.array(month)
#             y=list(np.unique(x))
#             distinct_date=[]
#             for i in y:
#                 distinct_date.append(i)

#         # print(distinct_date,'ashgjrdht')
#         if value=='year':
#             count_of_value1=df['Project/Function'].where(df['Project/Function']=='Management').groupby([df.Joining_Date.dt.year]).count()
#             count_of_value2=df['Project/Function'].where(df['Project/Function']=='Solar System').groupby([df.Joining_Date.dt.year]).count()
#             count_of_value3=df['Project/Function'].where(df['Project/Function']=='Venus').groupby([df.Joining_Date.dt.year]).count()
#             count_of_value4=df['Project/Function'].where(df['Project/Function']=='Uranus').groupby([df.Joining_Date.dt.year]).count()
#         elif value=='quarter':
#             count_of_value1=df['Project/Function'].where(df['Project/Function']=='Management').groupby([df.Joining_Date.dt.quarter]).count()
#             count_of_value2=df['Project/Function'].where(df['Project/Function']=='Solar System').groupby([df.Joining_Date.dt.quarter]).count()
#             count_of_value3=df['Project/Function'].where(df['Project/Function']=='Venus').groupby([df.Joining_Date.dt.quarter]).count()
#             count_of_value4=df['Project/Function'].where(df['Project/Function']=='Uranus').groupby([df.Joining_Date.dt.quarter]).count()
#         elif value=='month':
#             count_of_value1=df['Project/Function'].where(df['Project/Function']=='Management').groupby([df.Joining_Date.dt.month]).count()
#             count_of_value2=df['Project/Function'].where(df['Project/Function']=='Solar System').groupby([df.Joining_Date.dt.month]).count()
#             count_of_value3=df['Project/Function'].where(df['Project/Function']=='Venus').groupby([df.Joining_Date.dt.month]).count()
#             count_of_value4=df['Project/Function'].where(df['Project/Function']=='Uranus').groupby([df.Joining_Date.dt.month]).count()
#         else:
            
#             count_of_value1=df['Project/Function'].where(df['Project/Function']=='Management').groupby(df_date).count()
#             count_of_value2=df['Project/Function'].where(df['Project/Function']=='Solar System').groupby([date_range.date]).count()
#             count_of_value3=df['Project/Function'].where(df['Project/Function']=='Venus').groupby([date_range.date]).count()
#             count_of_value4=df['Project/Function'].where(df['Project/Function']=='Uranus').groupby([date_range.date]).count()
#         value1=[]
#         for i in count_of_value1:
#             value1.append(i)
#         value2=[]
#         for i in count_of_value2:
#             value2.append(i)
#         value3=[]
#         for i in count_of_value3:
#             value3.append(i)
#         value4=[]
#         for i in count_of_value4:
#             value4.append(i)
        
#         data=[]
#         for i in range(len(value1)):
#             data.append({'year':f'{value} {distinct_date[i]}','a':value1[i],'b':value2[i],'c':value3[i],'d':value4[i]})
#         print(data)
#         for i in data:

#             print(i)
        
#         context = {'segment': 'charts_from_file','type':type,'chart':True} 
#         context['chart_data']=json.dumps({
#         "element": "morris-bar-chart1",
#         "data":data,
#         "xkey": "year",
#         "barSizeRatio": 0.70,
#         "barGap": 3,
#         "resize": True,
#         "responsive": True,
#         "ykeys": ["a", "b", "c",'d'],
#         "labels": list(group),
#         "barColors": ["0-#1de9b6-#1dc4e9", "0-#899FD4-#A389D4", "#04a9f5"]
#         })
#         # print(context['chart_data'])
#         return render(request,'barchart.html',(context))


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////sample dynamic///////////////////////////////////////////////////////////


# def sample(request):
#     values=Currentemployees.objects.raw("SELECT id ,designation as position,EXTRACT(month FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees  GROUP BY designation,EXTRACT(month FROM joining_date)")
#     emp_count=[]
#     duration=[]
#     position=[]
#     for i in values:
#         emp_count.append(i.emp_count)
#         duration.append(i.duration)
#         position.append(i.position.strip())
#         print(i.position)
#     print((emp_count))
#     print(set(duration))
#     unique_duration=set(duration)
#     unique_duration=set(duration)
#     print(set(position))
#     data=[]
#     for i in values:
#         for j in range(len(unique_duration)):
#             if i.duration==list(unique_duration)[j]:
#                 data.append({'y':i.duration,'a':i.emp_count,'b':i.position.strip()})
#     print(data)
#     print(len(unique_duration),'len of unique_duration')
#     print(len(data),'len of data') 
#     final_data=[]
#     for i in range(len(unique_duration)):
#         final_data.append({})
    
    
#     for i in range(len(data)):
#         for j in range(len(unique_duration)):
#             final_data[j].update({"year":f"month {list(unique_duration)[j]}"})
#             if data[i]['y']==duration[j]:
#                 for z in range(len(position)):
#                     if data[i]['b']==position[z]:
#                         final_data[j].update({f'{position[z]}':data[i]['a']})
    
    
#     print(final_data)

    
#     return HttpResponse('welcome')
# "SELECT 
# 	designation,EXTRACT(year FROM joining_date)as year,count(emp_code) 
# FROM
# 	CURRENT_EMPLOYEES
# 			joining_date>DATEADD(Month, -12, getdate())
# GROUP BY
# 	designation,EXTRACT(year FROM joining_date);"


# def sample(request):
#     values=Currentemployees.objects.raw("SELECT id ,designation as position,EXTRACT(month FROM joining_date)as duration,count(emp_code) as emp_count FROM graph_currentemployees  GROUP BY designation,EXTRACT(month FROM joining_date)")
#     emp_count=[]
#     duration=[]
#     position=[]
#     for i in values:
#         emp_count.append(i.emp_count)
#         duration.append(i.duration)
#         position.append(i.position.strip())
#         print(i.position)
#     print((emp_count))
#     print(set(duration))
#     unique_duration=set(duration)
#     unique_duration=set(duration)
#     print(set(position))
#     data=[]
#     for i in values:
#         for j in range(len(unique_duration)):
#             if i.duration==list(unique_duration)[j]:
#                 data.append({'y':i.duration,'a':i.emp_count,'b':i.position.strip()})
#     print(data)
#     print(len(unique_duration),'len of unique_duration')
#     print(len(data),'len of data') 
#     final_data=[]
#     for i in range(len(unique_duration)):
#         final_data.append({})
    
    
#     for i in range(len(data)):
#         for j in range(len(unique_duration)):
#             final_data[j].update({"year":f"month {list(unique_duration)[j]}"})
#             if data[i]['y']==duration[j]:
#                 for z in range(len(position)):
#                     if data[i]['b']==position[z]:
#                         final_data[j].update({f'{position[z]}':data[i]['a']})
    
    
#     print(final_data)

    
#     return HttpResponse('welcome')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////bar cahrt ////////////////////////////////////////////////////////////////
# @csrf_exempt
# def bar1(request):
#     print('heloooooooooooooooooooooooooooooooooooooooooooooo')
#     import os
#     try:
#         if os.path.exists("media/updated_csv/current_employees.csv") or os.path.exists("media/updated_csv/resigned_employees.csv") :
#             os.remove("media/updated_csv/current_employees.csv")
#             os.remove("media/updated_csv/resigned_employees.csv")
#     except:
#         pass
#     else:
#         print('file does not exist')
#     write_csv() 
#     type='current'
#     try:
#         type1=request.POST['type']
#         type=type1
#         start_date=request.POST['startdate']
#         end_date=request.POST['enddate']
#         print(start_date,end_date,'iiiiiiiiiiiiiiiiiii')
#     except:
#         pass
   
#     if type=='current':
#         files=Currentemployees.objects.all()
#         if len(files)==0:
#             return render(request,'barchart.html',{'files':len(files)})
#     else:
#         files=Resignedemployees.objects.all()
#         if len(files)==0:
#             print('hiiiiiiiiiiiiiiiiiiiii')
#             return render(request,'barchart.html',{'files':len(files)})

#     try:
#         value=request.POST['value']
#         print(value)
#     except:
#         pass
   
#     print(value)
    
#     if type=='resigned':
#         table='media/updated_csv/resigned_employees.csv'
#     else:
#         table='media/updated_csv/current_employees.csv'
    
#     df=pd.read_csv(table)
#     df['Joining_Date'] = pd.to_datetime(df['Joining_Date'], errors='coerce')
#     group=df['Project_or_Function'].unique()
#     if value=='year':
#         year=df.Joining_Date.dt.year
#         x = np.array(year)
#         y=list(np.unique(x))
#         distinct_date=[]
#         for i in y:
#             distinct_date.append(i)
#     elif value=='quarter':
#         quarter=df.Joining_Date.dt.quarter
#         x = np.array(quarter)
#         y=list(np.unique(x))
#         distinct_date=[]
#         for i in y:
#             distinct_date.append(i)
#     else:
#         month=df.Joining_Date.dt.month
#         # print(month)
#         x = np.array(month)
#         y=list(np.unique(x))
#         distinct_date=[]
#         for i in y:
#             distinct_date.append(i)
    
    
#     total_count={}

#     for i in range(len(group)):
        
#         total_count[f'count_of_value{i}']=[]
    

  
#     if value=='month':
#         for i in range(len(group)):
#             total_count[f'count_of_value{i}'].extend(df['Project_or_Function'].where(df['Project_or_Function']==group[i]).groupby([df.Joining_Date.dt.month]).count())
#     elif value=='year':
#         for i in range(len(group)):
#             total_count[f'count_of_value{i}'].extend(df['Project_or_Function'].where(df['Project_or_Function']==group[i]).groupby([df.Joining_Date.dt.year]).count())
#     elif value=='quarter':
#         for i in range(len(group)):
#             total_count[f'count_of_value{i}'].extend(df['Project_or_Function'].where(df['Project_or_Function']==group[i]).groupby([df.Joining_Date.dt.quarter]).count())
#     else:
#         value='date'
#         start_date =start_date
#         end_date =end_date
#         mask = (df['Joining_Date'] > start_date) & (df['Joining_Date'] <= end_date)
#         df=df[mask]
#         if len(df)==0:
#             context={'files':0,'message':'No data between these two dates','type':type}
            
#             return render(request,'barchart.html',(context))
#         else:
#             month=df.Joining_Date.dt.date
#             # print(month)
#             x = np.array(month)
#             y=list(np.unique(x))
#             distinct_date=[]
#             for i in y:
#                 distinct_date.append(i)
#             for i in range(len(group)):
#                 total_count[f'count_of_value{i}'].extend(df['Project_or_Function'].where(df['Project_or_Function']==group[i]).groupby([df.Joining_Date.dt.date]).count())
    

#     data=[]
#     for i in range(len(total_count['count_of_value0'])):
#         data.append({})
   
#     for i in range(len(total_count['count_of_value0'])):
#         data[i].update({"year":f"{value} {distinct_date[i]}"})
#         for j in range(len(group)):
#             for z in range(len(total_count)):
#                 try:
#                     data[i].update({f'value{z}':total_count[f'count_of_value{z}'][i]})
#                 except:
#                     pass
#     print(data)

#     ###################################################################################################################


#     context = {'segment': 'charts_from_file','details':files,'type':type,'chart':True} 
#     context['chart_data']=json.dumps({
#     "element": "morris-bar-chart1",
#     "data":data,
#     "xkey": "year",
#     "barSizeRatio": 0.70,
#     "barGap": 3,
#     "resize": True,
#     "responsive": True,
#     "ykeys": [f'value{i}' for i in range(len(group))],
#     "labels": list(group),
#     "barColors": ["0-#1de9b6-#1dc4e9", "0-#899FD4-#A389D4", "#04a9f5"]
#     })
    