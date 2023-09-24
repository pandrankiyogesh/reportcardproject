from django.shortcuts import render
#render method is used to return the html files
from django.http import HttpResponse
def my_view(request):
    peoples=[{'name':'yogesh','age':67},
            {'name':'hima','age':20},
            {'name':'ramya','age':45},
            {'name':'tarun','age':21},
            {'name':'sailu','age':56}
            ]
    
    vegitables=['papaya','cabage','banana']
    return render(request,'index.html',context={'flower':peoples,'vegitables':vegitables,'titlee':'YOGESH'})#in the html file we are passing everything but what we want is declared in the html file
def contact_i(request):
    return render(request,'contact.html',context={'titlee':'CONTACT'})
def abou_t(request):
    return render(request,'about.html',context={'titlee':'ABOUT'})