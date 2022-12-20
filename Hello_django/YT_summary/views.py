from multiprocessing import context
import re
from django.http import HttpResponse, HttpResponseRedirect
import subprocess
from django.shortcuts import loader
from django.shortcuts import render
import json
import sys
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####
from django.views.generic import TemplateView
from subprocess import run,PIPE


def new(request):
    return render(request, "index.html")   

def index(request):
    template = loader.get_template('YT_exeten/popup.html') # getting our template  
    return HttpResponse(template.render())       # rendering the template in HttpResponse  

def disp(request):
    if request.method == 'POST':
        return HttpResponse('success post') # if everything is OK
    elif request.method == 'GET':
        return HttpResponseRedirect('')
        return HttpResponse('success')
    
    # nothing went well
    return HttpResponse('FAIL!!!!!')

    #return render(request, "index.html")    


#testing from video
def button(request):
    return render(request,'home.html')

def external(request):
    inp= request.POST.get('param')
    #out= run([sys.executable,'//mnt//e//work//djnago_testing//test.py',inp],shell=False,stdout=PIPE)
    out= run([sys.executable,'D://AA_Talha new//Degree 4th Sem//Subjects//python//Django//test.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'home.html',{'data1':out.stdout.decode('utf-8')})

#my try
def pop(request):
    return render(request,'popup.html')

def call(request):
    inpt= request.POST.get('arg')
    #outpt= run([sys.executable,'D://AA_Talha new//Degree 4th Sem//Subjects//python//Django//test.py',inpt],shell=False,stdout=PIPE)
    outpt= run([sys.executable,'D://AA_Talha new//Degree 4th Sem//Subjects//python//Python Codes//test.py',inpt],shell=False,stdout=PIPE)
    print(outpt)
    return render(request,'popup.html',{'data1':outpt.stdout.decode('utf-8')})

#with nltk
def disp(request):
    return render(request,'show.html')

def invok(request):
    inpt= request.POST.get('arg1')
    outpt= run([sys.executable,'D://AA_Talha new//Degree 4th Sem//Subjects//python//Django//summurize_byId.py',inpt],shell=False,stdout=PIPE)
    print(outpt)
    return render(request,'show.html',{'data1':outpt.stdout.decode('utf-8',errors="ignore")})

#format with nltk
def srch(request):
    return render(request,'srchbx.html')

def get_sum(request):
    inpt= request.POST.get('get_url')
    outpt= run([sys.executable,'D://AA_Talha new//Degree 4th Sem//Subjects//python//Django//summurize_byId.py',inpt],shell=False,stdout=PIPE)
    print(outpt)
    return render(request,'srchbx.html',{'data1':outpt.stdout.decode('utf-8',errors="ignore")})


# for test(success)
def h(request):
    return render(request, "hello.html")

def s(request):
    return HttpResponse("YASSS!")
   
    
        


