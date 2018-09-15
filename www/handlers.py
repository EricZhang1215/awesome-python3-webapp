#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'EricZhang'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from www.coroweb import get, post

from www.models import User, Comment, Blog, next_id

@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

#只要返回一个dict，后续的response这个middleware就可以把结果序列化为JSON并返回。
@get('/api/users')
def api_get_users():
    users = yield from User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)