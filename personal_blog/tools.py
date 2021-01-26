#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
    @Project    : FaceRecognition
    @Author     : Traiyi
    @Version    : 1.0
    @File       : tools.py
    @Desciption : 
    @Date       : 2021-01-26 22:03 
'''

# import lib
# from personal_blog.form import Log

from personal_blog.extensions import db

from personal_blog.models import Admin,Log

def add_log(ip,operate):
    log = Log(ip=ip,operate_user=get_operate_user(),operate=operate)
    db.session.add(log)
    db.session.commit()

def get_operate_user():
    with open('personal_blog/config', 'r') as f:
        id = f.read()
    admin = Admin.query.get(id)
    return admin.username
