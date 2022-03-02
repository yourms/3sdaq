from django.shortcuts import render, redirect
from .models import *
import sqlite3
# Create your views here.
def index(request):
    print(">>>> index")

    # if request.session.get('user_id') and request.session.get('user_name'):
    #     context = {
    #         'id' : request.session['user_id'],
    #         'name' : request.session['user_name']
    #     }
    #     return render(request, 'home.html', context)
    # else:
    #     return render(request, 'login.html')
    pass

def sTrade_list(request):
    print(">>>> sTrade_list")

    con = sqlite3.connect('./db.sqlite3')
    print("^^")
    cur = con.cursor()
    for row in cur.execute('select * from tradeApp_order '):
        print(row)
    # insert
    # into
    # tradeApp_order(code, gubun, price, quan, tquan, buyer, tradeyn, time1)
    # values(0001, 'B', 63000, 15, 0, 'minsu', 'N', (select datetime('now', 'localtime')))
    sTrade = Order.objects.all().order_by('-id')



    context = {
        'sTrades': sTrade
    }


    return render(request, 'sTrade/sTrade_list.html', context)




