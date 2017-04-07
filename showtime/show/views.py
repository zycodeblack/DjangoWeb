# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import django.shortcuts
import MySQLdb
# Create your views here.

def showdata(request):
	conn = MySQLdb.connect("localhost","root","411995202","dianyingtiantang")
	cur = conn.cursor()
	print "zhaoyu"
	n=cur.execute("select * from films")
	data = cur.fetchmany(n)
	for it in data:
	        print it[0]
	print "*****************"
	for it in data:
	        print it[1]
	cur.close()
	conn.close()
	
	return render_to_response("show.html",locals())
