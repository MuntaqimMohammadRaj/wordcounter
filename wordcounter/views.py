from django.http import HttpResponse
from django.shortcuts import render
import operator
def homeview(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def counter(request):
    data1=request.GET['textarea']
    data=data1.split()
    length=len(data)
    frequency={}
    for i in data:
        frequency[i]=(data.count(i))
   
    sorted_list=sorted(frequency.items(),key=operator.itemgetter(1))
    return render(request,'count.html',{'key':data1,'words':length,'i':sorted_list})