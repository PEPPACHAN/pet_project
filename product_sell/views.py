from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def add_products(recuest):
    return HttpResponse("Product added (no)")