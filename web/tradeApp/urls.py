from django.contrib import admin
from django.urls import path, include
from tradeApp import views
print("tra"
      ""
      "deApp urls")
urlpatterns = [
    # http://127.0.0.1:8000/trade/index
    path('index/', views.index, name='index'),
    path('', views.sTrade_list),
    path('sTrade_list/', views.sTrade_list, name='sTrade_list'),
    path('detail_order/', views.detail_order, name='detail_order'),
    path('sTrade_trade/', views.sTrade_trade, name='sTrade_trade'),

]
