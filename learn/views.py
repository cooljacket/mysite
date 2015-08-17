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

def home(request):
	superStar = "Python"
	li = ['C++', 'C', 'Java', 'Python', 'PHP', 'LISP'];
	return render(request, 'home.html', {'superStar': superStar, 'li': li})
