import os
import random
import sys
import sqlite3
from random import sample, randrange

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR : ", BASE_DIR)
dbURL = os.path.join(BASE_DIR , 'db.sqlite3')
print("dbURL : ", dbURL)
tradeAppURL = os.path.join(BASE_DIR , 'tradeApp')
print("tradeAppURL : " , tradeAppURL)
sys.path.append(tradeAppURL)
print(BASE_DIR)
con = sqlite3.connect(dbURL)

from views import query_sTrade_trade

#auto_sTrade_trade_print()
#query_sTrade_trade("user2", 76000, 10, 1, "B")


def price_list(now_price, b_or_s):
    price_list = []
    price_list.append(now_price)
    temp_price = now_price
    count = 1
    while count < 4 :
        count +=1
        if (temp_price <= 1000):
            temp_price -= 1
        elif (temp_price <= 5000):
            temp_price -= 5
        elif (temp_price <= 10000):
            temp_price -= 10
        elif (temp_price <= 50000):
            temp_price -= 50
        elif (temp_price <= 100000):
            temp_price -= 100
        elif (temp_price <= 500000):
            temp_price -= 500
        else :
            temp_price -= 5000
        price_list.append(temp_price)
    count = 1
    temp_price = now_price
    while count < 4:
        count += 1
        if (temp_price < 1000):
            temp_price += 1
        elif (temp_price < 5000):
            temp_price += 5
        elif (temp_price < 10000):
            temp_price += 10
        elif (temp_price < 50000):
            temp_price += 50
        elif (temp_price < 100000):
            temp_price += 100
        elif (temp_price < 500000):
            temp_price += 500
        else:
            temp_price += 5000
        price_list.append(temp_price)
    price_list.sort()
    if(b_or_s == "B") :
        select_price = random.choices(price_list, weights=[2, 3, 8, 15, 3, 1, 1], k=1)
    if (b_or_s == "S"):
        select_price = random.choices(price_list, weights=[1, 1, 3, 15, 8, 3, 2], k=1)
    print("price_list : ", select_price)
    return select_price[0]




cur = con.cursor()

b_or_s_list = ["B","S"]
user_list = []
comp_list = []


def list_setting():
    global user_list
    global comp_list

    sql_select = "select user_id from userApp_webuser"
    cur.execute(sql_select)

    for row in cur.fetchall():
        user_list.append(row[0])

    sql_select = "select code from tradeApp_comp"
    cur.execute(sql_select)
    for row in cur.fetchall():
        comp_list.append([row[0]])


def stock_auto_trade():
    ######################
    ######################
    ## K 값 조정하세요..!! ##
    ######################
    ######################
    trade_user_list = sample(user_list, k=1)
    global b_or_s_list
    print("stock_auto_trade")
    print("trade_user_list : ", trade_user_list)
    for user_id in trade_user_list:

        b_or_s = random.choice(b_or_s_list)
        print("var_b_or_s : ", b_or_s)

        selected_comp = sample(comp_list, k=1)

        print("selected_comp : ", selected_comp[0][0])
        code = selected_comp[0][0]


        query_txt = " select A.code, A.d_1price, ifnull(B.price, A.d_1price) as price"
        query_txt += " from tradeApp_comp A"
        query_txt += " left join tradeApp_order B on(A.code = B.code and B.time1 > (select strftime('%Y-%m-%d', 'now'))"
        query_txt += "    and B.quan = B.tquan and B.tradeyn='Y')"
        query_txt += " where A.code = ?"

        print("query_txt,  ", query_txt)
        cur.execute(query_txt, (code,))
        now_price = 0
        for row in cur.fetchall():
            now_price = row[2]
        print("now_price : ", now_price)

        price = price_list(now_price, b_or_s) # 가격 결정
        print("price_list : ", price)
        select_quan = randrange(10, 100, 10)  # 수량 결정
        print('user_id, price, select_quan, code, b_or_s : ', user_id, price, select_quan, code, b_or_s)
        query_sTrade_trade(user_id, price, select_quan, code, b_or_s)


from datetime import datetime
import time
now = datetime.now()
nowTime = now.strftime('%S')
list_setting()
while_count = 0
while True :
    now = datetime.now()
    nowTime = now.strftime('%S')
    #print("nowTime : ", nowTime)
    #print(nowTime == "30")
    #if(nowTime == "05" or nowTime == "10" or nowTime == "45" or nowTime == "00"):
    if(True):
        #while_count =  while_count + 1
        stock_auto_trade()
        #print(" while_count : ", while_count)
        #time.sleep(3)
    # else:
    #     while_count = 0
    #     print("nowTime : ", nowTime)













