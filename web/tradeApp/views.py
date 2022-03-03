from django.http      import JsonResponse
from django.shortcuts import render, redirect
from .models import *
import json
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
    typeST = request.POST.get('typeST', '')
    print("typeST : ", typeST)

    #sTrade = Order.objects.all().order_by('-id')
    market_price = query_market_price()
    #my_query = query_db(query_txt)
    #sTrade = json.dumps(my_query)
    # print(sTrade['code'])
    # print(json.dumps(sTrade, indent=2))
    #sTrade = json.dumps(my_query, ensure_ascii=False)

    context = {
        'sTrades': market_price
    }
    if(typeST == 'update'):
        return JsonResponse(market_price, safe=False)
    else:
        return render(request, 'sTrade/sTrade_list.html', context)

def detail_order(request):
    print(">>>> detail_order")
    code = request.POST['code']
    print('code : ', code)
    my_query = query_detail_order(code)
    print(my_query)
    jsonAry = []
    for value in my_query:
        print("value", value['code'])

    for value in my_query:
        jsonAry.append({
            'code': value['code'],
            'name': value['name'],
            'price': value['price'],
            'quan': value['quan'],
        })
    return JsonResponse(jsonAry, safe=False)

def query_db(query, args=(), one=False):
    print(">>>> query_db")
    con = sqlite3.connect('./db.sqlite3')
    cur = con.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

def query_market_price():
    # query_txt = "select * from tradeApp_order"
    # query_txt += " where tradeyn = 'Y' and code = 1"
    # query_txt += " order by time1 desc"
    # query_txt += " limit 1"

    query_txt = "select * from "
    query_txt += " (select A.code, B.name, A.price,B.d_1price, A.quan, (B.d_1price-A.price) AS change, round(CAST((B.d_1price-A.price) AS FLOAT)/CAST(B.d_1price AS FLOAT) * 100, 2) as ch_rate"
    query_txt += " from tradeApp_order A"
    query_txt += " join tradeApp_comp B on(A.code = B.code)"
    query_txt += " where tradeyn = 'Y'"
    query_txt += " order by time1 desc)"
    query_txt += " group by code"
    return query_db(query_txt)

def query_detail_order(code):
    # query_txt = "select * from tradeApp_order"
    # query_txt += " where tradeyn = 'Y' and code = 1"
    # query_txt += " order by time1 desc"
    # query_txt += " limit 1"


    query_txt = " select A.code, B.name, A.price,B.d_1price, (A.quan - A.tquan) as quan"
    query_txt += " from tradeApp_order A"
    query_txt += " join tradeApp_comp B on(A.code = B.code)"
    query_txt += " where A.quan != A.tquan"
    query_txt += " and A.code = "+code
    query_txt += " order by A.price desc"
    print(query_txt)
    return query_db(query_txt)


