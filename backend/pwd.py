#Author:Jason Song
import pymysql
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
import os
import hashlib
import json
file_path = os.path.realpath(__file__)
path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
file = open(path+"\db_set\db.py",'r')
content = file.readlines()[0]
db_data = eval(content)
file.close()



def db_login():
    try:
        db = pymysql.connect(db_data['server'], db_data['user_name'], db_data['pwd'], "study", charset='utf8')
    except Exception as e:
        os.system('reboot')
    return db


def pwd(request):
    res = json.loads(request.body)
    user_name = res["user_name"]
    password = res["password"]
    m = hashlib.md5()
    b = password.encode(encoding='utf-8')
    m.update(b)
    password_md5 = m.hexdigest()
    db = db_login()
    cursor = db.cursor()
    sqlexist = "select id,username,`type` from jx3_admin where username = '%s' and password = '%s'" % (
        user_name, password_md5)
    res = cursor.execute(sqlexist)
    if res == 1:
        admin_id = cursor.fetchall()[0][0]
        cursor.close()
        db.close()
    else:
        admin_id = 0
    if admin_id != 0:
        db = db_login()
        cursor = db.cursor()
        sql = "select * from jx3_pwd where admin = %s order by owner"%admin_id
        cursor.execute(sql)
        list = cursor.fetchall()
        cursor.close()
        db.close()
        pwd_list = []
        for i in list:
            pwd_list.append(
                    {
                        "id":i[0],
                        "user_name":i[1],
                        "pwd":i[2],
                        "owner":i[3],
                        "ex":i[4],
                    }
            )
        msg = {
            "data": pwd_list,
            "code": 20000,
        }
        return JsonResponse(msg, safe=False)


    else:
        msg = {
            "data": [],
            "code": 50008,
        }
        return JsonResponse(msg, safe=False)
