from django.urls import path,re_path
from . import views

urlpatterns=[
   
    path('',views.index,name=''),
    path('get_column',views.get_column,name='get_column'),
    path('current',views.current,name='current'),
    path('resigned',views.resigned,name='resigned'),
    path('que',views.query,name='que'),
    path('bar',views.bar,name='bar'),
    path('chart',views.chart,name='chart'),
    path('new',views.new),
    re_path(r'pie_charrt/(?P<string>[\w\-]+)/$',views.piechart,name='pie_chart'),
    path('bar_duration',views.bar_duration,name='bar_duration'),
    re_path(r'^pay/summary/(?P<string>[\w\-]+)/$', views.pay_summary, name='pay_summary')




   
]