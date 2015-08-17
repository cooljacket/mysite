# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse(u'Welcome, Jacket')

def cacl(request):
	a = request.GET['a']
	b = request.GET['b']
	return HttpResponse(str(int(a) + int(b)))

def cacl2(request, a, b):
	return HttpResponse(str(int(a) + int(b)))