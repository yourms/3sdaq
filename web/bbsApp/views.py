from django.shortcuts import render, redirect
from django.http      import JsonResponse
import os
import sqlite3
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbURL = os.path.join(BASE_DIR , 'db.sqlite3')
# Create your views here.




def index(request) :
   return render(request, 'index2.html')

def login(request) :
    return render(request, 'login2.html')



# 여기에서 sqlite 값 가져오면 될듯? ?
def charts(request) :
    installation = [3068, 2970, 2839, 2977, 2663 , 2665 ]
    context = {
        'installation' : installation
    }
    return render(request,  'charts.html', context)
def myLineChart(request) :
    print(">>>>> myLineChart")

    con = sqlite3.connect(dbURL)
    cur = con.cursor()
    query_txt = " select day, ex_index from tradeApp_d_trade"
    cur.execute(query_txt)
    labels = []
    ex_index = []
    for row in cur.fetchall():
        labels.append(row[0])
        ex_index.append(row[1])
    print("labels : ", labels)
    print("ex_index : ", ex_index)
    cur.connection.close()
    con.close()

    jsonAry = []
    my_query = []
    #my_query = [{"id":3000}]
    #for value in my_query:
    jsonAry.append({
        'labels' : labels,
        'ex_index': ex_index
    })
    print(jsonAry)
    return JsonResponse(jsonAry, safe=False)
